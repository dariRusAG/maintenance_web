from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.event_model import *
from models.admin_profile_model import *


@app.route('/admin_profile', methods=['GET', 'POST'])
def admin_profile():
    conn = get_db_connection()

    # Начальная инициализация параметров
    admin_panel_button = None
    df_theme = get_theme_for_admin(conn)
    df_type = get_type_for_admin(conn)
    df_organizer = get_organizer_for_admin(conn)
    df_location = get_location_for_admin(conn)
    df_status = get_status_for_admin(conn)
    df_user_event = get_users_events(conn)
    detailed_info = False
    checked_value = False

    if 'event_id' not in session:
        session['event_id'] = 0

    if request.values.get('panel'):
        admin_panel_button = request.values.get('panel').title()

    if request.values.get('add_new_event'):
        location_name = df_location.loc[int(request.values.get('location')) - 1][0]
        venue_name = str(request.values.get('new_event_venue'))
        add_new_venue(conn, venue_name)
        venue_id = int(get_venue_id(conn, venue_name))
        add_new_location(conn, venue_id, location_name)
        get_location_id(conn, venue_id, location_name)
        print(get_location_id(conn, venue_id, location_name))
        add_new_event(conn, request.values.get('new_event_name'), request.values.get('theme'),
                      request.values.get('type'), request.values.get('new_event_part'),
                      request.values.get('new_event_beginning_date')[6:11] + "-" + request.values.get(
                          'new_event_beginning_date')[3:5] + "-" + request.values.get('new_event_beginning_date')[0:2],
                      request.values.get('new_event_expiration_date')[6:11] + "-" + request.values.get(
                          'new_event_expiration_date')[3:5] + "-" + request.values.get('new_event_expiration_date')[
                                                                    0:2],
                      request.values.get('start_time'), request.values.get('end_time'), request.values.get('organizer'),
                      int(get_location_id(conn, venue_id, location_name)), request.values.get('new_event_description'),
                      request.values.get('status'), request.values.get('picture'))

        admin_panel_button = "Добавление"

    elif request.values.get('delete_event'):
        session['event_id'] = int(request.values.get('delete_event'))
        admin_panel_button = "Редактирование"
        delete_event(conn, session['event_id'])

    # нажата кнопка подробнее
    elif request.values.get('choice_event'):
        session['event_id'] = int(request.values.get('choice_event'))
        admin_panel_button = "Редактирование"

    elif request.values.get('choice_event_suggest'):
        session['event_id'] = int(request.values.get('choice_event_suggest'))
        admin_panel_button = "Предложения"

    elif request.values.get('add_suggest_event'):
        session['event_id'] = int(request.values.get('add_suggest_event'))
        admin_panel_button = "Предложения"
        update_suggest_event(conn, session['event_id'])

    elif request.values.get('delete_suggest_event'):
        session['event_id'] = int(request.values.get('delete_suggest_event'))
        admin_panel_button = "Предложения"
        delete_event(conn, session['event_id'])

    # нажата кнопка редактирования мероприятия
    elif request.values.get('is_edit_event'):
        checked_value = True
        session['event_id'] = request.values.get('is_edit_event')
        admin_panel_button = "Редактирование"

    elif request.values.get('edit_event'):
        admin_panel_button = "Редактирование"
        location_name = df_location.loc[int(request.values.get('edit_location')) - 1][0]
        venue_name = str(request.values.get('edit_event_venue'))
        add_new_venue(conn, venue_name)
        venue_id = int(get_venue_id(conn, venue_name))
        add_new_location(conn, venue_id, location_name)
        get_location_id(conn, venue_id, location_name)
        print(request.values.get('edit_type'))
        print(request.values.get('edit_theme'))
        update_event(conn, session['event_id'], request.values.get('edit_event_name'), request.values.get('edit_theme'),
                     request.values.get('edit_type'), request.values.get('edit_event_participants'),
                     request.values.get('edit_event_beginning_dat')[6:11] + "-" + request.values.get(
                         'edit_event_beginning_dat')[3:5] + "-" + request.values.get('edit_event_beginning_dat')[0:2],
                     request.values.get('edit_event_expiration_dat')[6:11] + "-" + request.values.get(
                         'edit_event_expiration_dat')[3:5] + "-" + request.values.get('edit_event_expiration_dat')[0:2],
                     request.values.get('edit_event_start_time'), request.values.get('edit_event_end_time'),
                     request.values.get('edit_organizer'),
                     int(get_location_id(conn, venue_id, location_name)), request.values.get('edit_event_description'),
                     request.values.get('edit_status'), request.values.get('edit_event_picture'))

    event_info = get_event_info(conn, session['event_id'])
    df_event = get_event(conn)
    df_participants = get_participants(conn)
    df_suggest_event = get_suggest_event(conn)

    html = render_template(
        'admin_profile.html',
        admin_panel_button=admin_panel_button,
        theme_list=df_theme,
        type_list=df_type,
        organizer_list=df_organizer,
        location_list=df_location,
        status_list=df_status,
        user_rate=df_user_event,
        all_events=df_event,
        detailed_info=detailed_info,
        event_info=event_info,
        participants_list=df_participants,
        checked_value=checked_value,
        one_event_info=event_info,
        suggest_event=df_suggest_event,
        len=len
    )

    return html
