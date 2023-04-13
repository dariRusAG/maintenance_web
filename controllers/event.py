from app import app
from flask import render_template, request, session, make_response
from utils import get_db_connection
from models.event_model import *

@app.route('/', methods=['GET', 'POST'])
def event():
    conn = get_db_connection()
    # переменная для окна входа
    user_login = False
    # неправильный логин
    error_info = False

    event_id = 0
    info_ = 0
    df_users = get_users(conn)

        # нажата кнопка Найти
    # if request.values.get('status'):
    #     status = int(request.values.get('status'))


        # нажата кнопка подробнее
    if request.values.get('choice_event'):
        event_id = int(request.values.get('choice_event'))
        info_ = 1

        # нажата кнопка участия
    elif request.values.get('registration'):
        event_id = int(request.values.get('registration'))
        if 'user_id' in session:
            to_registrate(conn,session['user_id'],event_id)
        else:
            user_login = True
            session['remember_id'] = event_id

        # если пользователь вышел
    elif request.values.get('user_logout'):
        session.pop('user_id', None)
        session['types'] = []
        session['themes'] = []
        session['organizers'] = []
        session['locations'] = []
        session['status'] = []
        session['start_date'] = "0000-00-00"
        session['end_date'] = "9999-99-99"
        session['start_time'] = "00:00"
        session['end_time'] = "23:59"

        # нажата кнопка отменить
    elif request.values.get('cancel'):
        event_id = int(request.values.get('cancel'))
        to_cancel(conn,session['user_id'],event_id)

        # нажата кнопка войти
    elif request.values.get('user_login'):
        user_login = True


    elif request.values.get('login'):
        login = request.values.get('login')
        password = request.values.get('password')
        print(login)
        match is_correct_login_and_password(conn, login, password):
            case "user":
                session['user_id'] = f'{get_user_id(conn, login)}'
                session['user_role'] = "user"
                if 'remember_id' in session:
                    if len(is_was_registarte_to_event(conn, session['user_id'], session['remember_id'])) == 0:
                        to_registrate(conn, session['user_id'], session['remember_id'])
                    session.pop('remember_id', None)
            case "admin":
                session['user_id'] = f'{get_user_id(conn, login)}'
                session['user_role'] = "admin"
            case "error":
                error_info = True
                user_login = True

    # нажата кнопка Очистить
    if request.form.get('clear'):
        types = []
        themes = []
        organizers = []
        locations = []
        status = []
        session['types'] = []
        session['themes'] = []
        session['organizers'] = []
        session['locations'] = []
        session['status'] = []
        session['start_date'] = "0000-00-00"
        session['end_date'] = "9999-99-99"
        session['start_time'] = "00:00"
        session['end_time'] = "23:59"
    else:
        types = request.form.getlist("Тип")
        themes = request.form.getlist("Тема")
        organizers = request.form.getlist("Организатор")
        locations = request.form.getlist("Площадка")
        status = request.form.getlist("Статус")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")

    if request.form.get('search'):
        session['types'] = types
        session['themes'] = themes
        session['organizers'] = organizers
        session['locations'] = locations
        session['status'] = status
        if start_date != '':
            session['start_date'] = start_date[6:11] + "-" + start_date[3:5]+ "-" + start_date[0:2]
        if end_date != '':
            session['end_date'] = end_date[6:11] + "-" + end_date[3:5] + "-" + end_date[0:2]
        if start_time != '':
            session['start_time'] = start_time
        if end_time != '':
            session['end_time'] = end_time

    # если пользователь не вошел, то он гость
    if 'user_id' not in session:
        session['user_role'] = "guest"

    # ивенты пользователя (для кнопки отмены)
    if 'user_id' in session:
        df_user_event = get_user_events_only_id(conn,session['user_id'])
        df_user_event = df_user_event.values.tolist()
    else:
        df_user_event = []

    if 'types' not in session:
        session['types'] = []
    if 'themes' not in session:
        session['themes'] = []
    if 'organizers' not in session:
        session['organizers'] = []
    if 'locations' not in session:
        session['locations'] = []
    if 'status' not in session:
        session['status'] = []
    if 'start_date' not in session:
        session['start_date'] = "0000-00-00"
    if 'end_date' not in session:
        session['end_date'] = "9999-99-99"
    if 'start_time' not in session:
        session['start_time'] = "00:00"
    if 'end_time' not in session:
        session['end_time'] = "23:59"

    df_theme = get_theme(conn)
    df_type = get_type(conn)
    df_organizer = get_organizer(conn)
    df_location = get_location(conn)
    df_status = get_status(conn)
    event_info = get_event_info(conn, event_id)
    df_event = get_event(conn)
    df_participants = get_participants(conn)

    df_event = df_event[((df_event['type_name'].isin(session['types'])) | (len(session['types']) == 0)) & (
            (df_event['theme_name'].isin(session['themes'])) | (len(session['themes']) == 0)) & (
            (df_event['organizer_name'].isin(session['organizers'])) | (len(session['organizers']) == 0)) & (
            (df_event['location_name'].isin(session['locations'])) | (len(session['locations']) == 0)) & (
            (df_event['status_name'].isin(session['status'])) | (len(session['status']) == 0)) & (
            (df_event['start_time'] >= session['start_time'])) & (df_event['end_time'] <= session['end_time']) & (
            (df_event['beginning_date'] >= session['start_date'])) & (df_event['expiration_date'] <= session['end_date'])]


    html = render_template(
        'event.html',
        theme_list=df_theme,
        type_list=df_type,
        organizer_list=df_organizer,
        location_list=df_location,
        status_list=df_status,
        events=df_event,
        event_info=event_info,
        info_=info_,
        user_login=user_login,
        error_info=error_info,
        user_event_list=df_user_event,
        participants_list=df_participants,
        user_role=session['user_role'],
        len=len
    )

    return html