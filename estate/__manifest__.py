{
    'name': 'Estate',
    'version': '',
    'summary': 'estate property module',
    'description': '',
    'depends': ['base', 'mail', 'web','product'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/property.tag.csv',
        'wizard/delete_property_wizard_view.xml',
        'views/estate_property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/users_inherited_view.xml',
        'views/menu_view.xml',
        'views/external_layout_standard_inherited.xml',
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
    ],
    'assets': {
        'web.assets_common': [
            'estate/static/src/css/style.css',
        ],

    },
    'demo': [],
    'installable': True,
    'auto_install': False,
}
