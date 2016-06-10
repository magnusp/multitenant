# -*- coding: utf-8 -*-

import functools

from flask import redirect, request, render_template, make_response, g

from factory import create_app
from model import db, Tenant

app = create_app('multitenant')


def requires_tenant(*args, **kwargs):
    def wrapper(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            tenant_id = request.cookies.get('tenant_id', None)
            if not tenant_id:
                return redirect('/')
            tenant_name = request.headers.get('X-TENANT-NAME', None)
            lookup_made = False
            if not tenant_name:
                db.session.execute('SELECT pg_sleep(1)')
                tenant = Tenant.query.filter_by(id=tenant_id).first()
                g.tenant_name = tenant.name
                lookup_made = True
            resp = make_response(f(*args, **kwargs))
            resp.headers['X-TENANT-LOOKUP'] = 'yes' if lookup_made else 'no'
            return resp
        return wrapped
    return wrapper


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', name="Joe")

    tenant = Tenant.query.filter_by(id=request.form.get('tenant_id', None)).first()
    if tenant:
        resp = make_response(redirect('/resource'))
        resp.set_cookie('tenant_id', str(tenant.id))
        return resp
    return redirect('/')


@app.route('/resource')
@requires_tenant()
def tenant_resource():
    return "OK: '%s'" % g.tenant_name