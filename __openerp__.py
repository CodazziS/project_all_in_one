{
    'name': "Project All in one",
    'author' : 'Stéphane Codazzi @ TeMPO-consulting',
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
        'project_indicators',
        'project_logical_framework',
        'project_finances',
        'project_partners'],
    'data': [
        'static/src/xml/view.xml', 
    ],
}
