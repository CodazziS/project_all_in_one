{
    'name': "Project All in one",
    'author' : 'Stéphane Codazzi @ TeMPO-Consulting',
    'category': 'Project',
    'sequence': 1,
    'description': """
Project Indicators
===================

Install addons :

* project
* project_indicators
* project_logical_framework
* project_finances
* project_partners

    """,
    'version': '0.3',
    'depends': [
        'project',
        'odoo-project_indicators',
        'odoo-project_logical_framework',
        'odoo-project_finances',
        'odoo-project_partners'],
    'data': [
        'static/src/xml/view.xml', 
    ],
}
