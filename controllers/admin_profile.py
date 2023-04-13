from app import app
from flask import render_template, request
from utils import get_db_connection
from models.event_model import *

@app.route('/admin_profile', methods=['GET', 'POST'])
def admin_profile():
    conn = get_db_connection()
    admin_panel_button = None
    df_theme = get_theme(conn)
    df_type = get_type(conn)
    df_organizer = get_organizer(conn)
    df_location = get_location(conn)
    df_status = get_status(conn)

    if request.values.get('panel'):
        admin_panel_button = request.values.get('panel').title()

    if request.values.get('add_new_event'):
        print(request.values.get('new_event_name'))
        print(request.values.get('theme'))
        print(request.values.get('type'))
        print(request.values.get('organizer'))
        print(request.values.get('location'))
        print(request.values.get('new_event_venue'))
        print(request.values.get('status'))
        print(request.values.get('new_event_part'))
        print(request.values.get('new_event_beginning_date'))
        print(request.values.get('new_event_expiration_date'))
        print(request.values.get('start_time'))
        print(request.values.get('end_time'))
        print(request.values.get('new_event_description'))
        admin_panel_button = "Добавление"

    html = render_template(
        'admin_profile.html',
        admin_panel_button=admin_panel_button,
        theme_list=df_theme,
        type_list=df_type,
        organizer_list=df_organizer,
        location_list=df_location,
        status_list=df_status,
        len=len
    )

    return html