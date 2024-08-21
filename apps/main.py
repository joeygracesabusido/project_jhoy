from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse

# from .routes.login import api
# from .routes.admin import api
# from .routes.login import login_router
from apps.routes.admin import api
from apps.routes.login import login_router
from apps.routes.inventory import api_invt
from apps.routes.job_order_temp import api_jo_temp
from apps.routes.job_order import api_job_order
from apps.routes.payroll_template import api_payroll_temp
from apps.routes.payroll import api_payroll

from apps.routes.graphql import graphql_app

from apps.routes.inventory_temp import api_inventory

from apps.routes.purchase_order_temp import api_purchase_ord_temp
from apps.routes.purchase_order import api_purchase_order


from apps.routes.accounting.chart_of_account import api_chart_of_account
from apps.routes.accounting.insert_account_type import api_account_type


from apps.routes.accounting.accounting_templ import api_accounting_temp


from apps.routes.accounting.journal_entry import api_journale_entry

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="apps/static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)



app.include_router(api, tags=["admin"])
app.include_router(login_router)
app.include_router(api_inventory)
app.include_router(api_invt, tags=['inventory'])
app.include_router(api_jo_temp)
app.include_router(api_job_order, tags=['Job Order'])
app.include_router(api_payroll_temp)
app.include_router(api_payroll, tags=['paryoll'])

app.include_router(api_purchase_ord_temp)
app.include_router(api_purchase_order, tags=['Purchase Order'])


app.include_router(api_accounting_temp)

app.include_router(api_account_type, tags=['Type of Account'])
app.include_router(api_chart_of_account, tags=['Chart of Account'])


app.include_router(api_journale_entry, tags=['Journal Entry'])


# Mount Strawberry's GraphQL app onto FastAPI
app.mount("/graphql", graphql_app)


