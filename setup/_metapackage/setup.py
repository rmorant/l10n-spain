import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-l10n-spain",
    description="Meta package for oca-l10n-spain Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_invoice_import_facturae',
        'odoo12-addon-account_promissory_note_bankia',
        'odoo12-addon-account_promissory_note_caixabank',
        'odoo12-addon-account_promissory_note_deutschebank_es',
        'odoo12-addon-account_promissory_note_santander',
        'odoo12-addon-delivery_gls_asm',
        'odoo12-addon-delivery_seur',
        'odoo12-addon-l10n_es_account_asset',
        'odoo12-addon-l10n_es_account_bank_statement_import_n43',
        'odoo12-addon-l10n_es_account_banking_sepa_fsdd',
        'odoo12-addon-l10n_es_account_invoice_sequence',
        'odoo12-addon-l10n_es_aeat',
        'odoo12-addon-l10n_es_aeat_mod111',
        'odoo12-addon-l10n_es_aeat_mod115',
        'odoo12-addon-l10n_es_aeat_mod123',
        'odoo12-addon-l10n_es_aeat_mod130',
        'odoo12-addon-l10n_es_aeat_mod190',
        'odoo12-addon-l10n_es_aeat_mod216',
        'odoo12-addon-l10n_es_aeat_mod296',
        'odoo12-addon-l10n_es_aeat_mod303',
        'odoo12-addon-l10n_es_aeat_mod303_oss',
        'odoo12-addon-l10n_es_aeat_mod347',
        'odoo12-addon-l10n_es_aeat_mod349',
        'odoo12-addon-l10n_es_aeat_mod390',
        'odoo12-addon-l10n_es_aeat_partner_check',
        'odoo12-addon-l10n_es_aeat_sii',
        'odoo12-addon-l10n_es_aeat_sii_extra_data',
        'odoo12-addon-l10n_es_aeat_sii_oss',
        'odoo12-addon-l10n_es_aeat_vat_prorrate',
        'odoo12-addon-l10n_es_aeat_vat_prorrate_asset',
        'odoo12-addon-l10n_es_dua',
        'odoo12-addon-l10n_es_dua_sii',
        'odoo12-addon-l10n_es_dua_ticketbai_batuz',
        'odoo12-addon-l10n_es_extra_data',
        'odoo12-addon-l10n_es_facturae',
        'odoo12-addon-l10n_es_facturae_efact',
        'odoo12-addon-l10n_es_facturae_face',
        'odoo12-addon-l10n_es_intrastat_report',
        'odoo12-addon-l10n_es_irnr',
        'odoo12-addon-l10n_es_location_nuts',
        'odoo12-addon-l10n_es_mis_report',
        'odoo12-addon-l10n_es_partner',
        'odoo12-addon-l10n_es_partner_mercantil',
        'odoo12-addon-l10n_es_pos',
        'odoo12-addon-l10n_es_subcontractor_certificate',
        'odoo12-addon-l10n_es_ticketbai',
        'odoo12-addon-l10n_es_ticketbai_api',
        'odoo12-addon-l10n_es_ticketbai_api_batuz',
        'odoo12-addon-l10n_es_ticketbai_batuz',
        'odoo12-addon-l10n_es_ticketbai_pos',
        'odoo12-addon-l10n_es_toponyms',
        'odoo12-addon-l10n_es_vat_book',
        'odoo12-addon-l10n_es_vat_book_extra_data',
        'odoo12-addon-payment_redsys',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
