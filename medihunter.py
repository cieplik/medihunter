""" Base script without pushover notifications
this is a startpoint for adding new features
"""

import json
import time
from datetime import datetime, timedelta
from typing import Callable, List
import urllib.parse



params = json.load(open("/home/dawid/git/medihunter/ids/params.json"))


# import click
#
# from medicover_session import (
#     Appointment,
#     MedicoverSession,
#     load_available_search_params,
# )
# from medihunter_notifiers import pushover_notify, telegram_notify, xmpp_notify
#
# now = datetime.now()
# now_formatted = now.strftime("%Y-%m-%dT02:00:00.000Z")
#
#
# def make_duplicate_checker() -> Callable[[Appointment], bool]:
#     """Closure which checks if appointment was already found before
#
#     Returns:
#         True if appointment ocurred first time
#         False otherwise
#     """
#     found_appointments: List[Appointment] = []
#
#     def duplicate_checker(appointment: Appointment) -> bool:
#         if appointment in found_appointments:
#             return False
#         found_appointments.append(appointment)
#         return True
#
#     return duplicate_checker
#
#
# duplicate_checker = make_duplicate_checker()
#
#
# def notify_external_device(message: str, notifier: str, **kwargs):
#     # TODO: add more notification providers
#     if notifier == "pushover":
#         title = kwargs.get("notification_title")
#         pushover_notify(message, title)
#     elif notifier == "telegram":
#         telegram_notify(message)
#     elif notifier == "xmpp":
#         xmpp_notify(message)
#
rating = {
    "Bronikowska Paulina": "5.0 (44)",
    "Borowski Włodzimierz": "G:2.3 (4)",
    "Droszcz-Karsz Elżbieta": "5.0 (9)",
    "Drozdowska Katarzyna": "5.0 (9)",
    "Lelito Katarzyna": "2.5 (7)",
    "Jarecka-Szmajdzińska Katarzyna": "2.5 (21)",
    "Monticolo Marta": "5 (3)",
    "Opatczyk Paweł": "3.5 (12)",
    "Krysztopowicz-Sobura Katarzyna": "4.0 (16)",
    "Chudzicka Aleksandra": "4.0 (4)",
    "Mazur Dariusz": "5.0 (23)",
    "Zembrzuski Ryszard": "MC:4.0 (161)",
    "Piskorska-Ślesicka Joanna": "5.0 (8)",
    "Duda Beata": "5.0 (9)",
    "Horszczaruk Dariusz": "MC:3.5 (44)",
    "Moskal Wojciech": "MC:4.5 (186)",
    "Guranowski Tomasz": "3.5 (7)",
    "Piotrowska-Karaś Anna": "3.5 (18)",
    "Gapińska Katarzyna": "5.0 (6)",
    "Kraśniewska Karolina": "(0)",
    "Tarasenko Sergii": "(0)",
    "Łyjak Piotr": "5.0 (12)",
    "Frączek Anna": "(0)",
    "Grunwald-Gustafsson Danuta": "4.0 (8)",
    "Fiuk-Gliwińska Małgorzata": "(0)",
    "Śliwińska-Wasilewska Anna": "4.0 (5)",
    "Fabijańska Anna": "5.0 (15)",
    "Kownacka-Stobnicka Elżbieta": "5.0 (2)",
    "Dmowska-Koroblewska Agnieszka": "5.0 (46)",
    "Stojek Arkadiusz": "MC:5.0 (177)",
    "Woźniak Artur": "3.5 (16)",
    "Szeptycka-Adamus Alicja": "4.0 (7)",
    "Męczkowska Katarzyna": "MC:4.5 (78)",
    "Faliszewska Judyta": "MC:4.0 (75)",
    "Leszczyńska Iwona": "1.0 (23)",
    "Galak Danuta": "3.5 (14)",
    "Gawrych Piotr": "4.0 (10)",
    "Gliwicz-Miedzińska Dorota": "5.0 (5)",
    "Grzelczyk - Wielgórska Monika": "5.0 (8)",  # ID 227640
    "Gąsior Robert": "5.0 (20)",
    "Jarrah Sami": "5.0 (13)",
    "Kalbarczyk Anna": "3.0 (10)",
    "Kasprzycka Agnieszka": "5.0 (31)",
    "Lipka Joanna": "5.0 (3)",
    "Leśniak Tomasz": "(0)",
    "Rojek Dorota": "5.0 (12)",
    "Wantuch Maciej": "(0)",
    "Wojtyczka Michał": "(0)",
    "Żubka Magdalena": "(0)",
    "Fijałkowska Elżbieta": "5.0 (31)",
    "Tomaszewska Ewa": "5.0 (11)",
    "Roman Artur": "MC:5.0 (222)",
    "Hoppe Robert": "5.0 (29)",
    "Kenig Dagmara": "5.0 (24)",
    "Kokieć - Korycińska Anna": "(0)",
    "Kowalska Ewa": "1.5 (5)",
    "Kroczek Sylwia": "(0)",
    "Lebelt - Pieniąca Katarzyna": "RL:5.0 (2)",
    "Mekrouda Magda": "(0)",
    "Monkiewicz - Kołodziejczyk Hanna": "2.0 (11)",
    "Nagraba Katarzyna": "(0)",
    "Nikończyk Monika": "5.0 (4)",
    "Nowacka Maria": "4.5 (9)",
    "Ogińska Zdzisława": "3.5 (26)",
    "Okrzeja Dariusz": "5.0 (18)",
    "Olszewska Monika": "4.5 (33)",
    "Przewoźna Joanna": "G:3.2 (9)",
    "Runowski Dariusz": "5.0 (11)",
    "Ryszkowska Anna": "4.0 (5)",
    "Sienicka Justyna": "(0)",
    "Sobczyk Grzegorz": "4.0 (25)",
    "Stolarska-Kraszewska Lidia": "5.0 (27)",
    "Sychowicz Cezary": "5.0 (11)",
    "Sykson Ewa": "3.0 (13)",
    "Szarla Anna": "(0)",
    "Wątrobińska Urszula": "RL:5.0 (8)",
    "Zawadowski Jacek": "3.0 (18)",
    "Zegadło Marcin": "4.0 (16)",
    "Ziemiańska Agata": "(0)",
    "Łysenko - Pośnik Uljana": "(0)",
}


from fasthtml.common import *
app, rt = fast_app()

@rt("/bam")
def get():
    return "BAM!"

@rt("/delete")
def delete():
    return ""

@rt("/available_specializations")
def get(patient: str = None, specialization: str = None):
    selections = [
        Select(
            Option("Wybierz pacjenta", value="", hidden=True, disabled=True, selected=True),
            Option("Dawid", value="Dawid"),
            Option("Magda", value="Magda"),
            Option("Szymon", value="Szymon"),
            name="patient",
            id="select_patient",
            hx_get="/available_specializations",
            hx_target="closest tr",
            hx_preserve=True
        )
    ]

    if not patient:
        return Td(*selections), Td()

    if patient == "Dawid":
        specializations = params["availableSpecializations"][:10]
    elif patient == "Magda":
        specializations = params["availableSpecializations"][10:20]
    else:
        specializations = params["availableSpecializations"][20:]

    selections += [
        Select(
            Option("Wybierz specializację", value="", hidden=True, disabled=True, selected=True),
            *[Option(s["text"], value=f'{s["text"]} ({s["id"]})') for s in specializations if s["id"] > 0],
            name="specialization",
            id="select_specialization_" + patient,
            hx_get="/available_specializations?patient=" + patient,
            hx_target="closest tr",
            hx_preserve=True
        )
    ]

    if not specialization:
        return Td(*selections), Td()

    mammoth = "🦣"
    return Td(*selections), Td(Button(mammoth, hx_post="/hunt?patient=" + patient + "&specialization=" + urllib.parse.quote_plus(specialization),
                                      hx_target="closest tr", hx_swap="beforebegin"))

@rt("/hunt")
def post(patient: str, specialization: str):
    return Tr(
        Td(patient + ": " + specialization),
        Td(Button("✖", hx_delete="/delete", hx_target="closest tr", hx_swap="outerHTML"))
    )

@rt("/")
def get():
    return Div(
        Table(
            Thead(Tr(Th("medihunter"), Th())),
            Tbody(Tr(hx_trigger="load", hx_get="/available_specializations"))
        ),
    )

serve(port=20183)
serve(host="2a01:4f9:2b:27a9::183", port=20183)


#
# def process_appointments(
#     appointments: List[Appointment], iteration_counter: int, notifier: str, **kwargs
# ):
#
#     applen = len(appointments)
#     click.echo(
#         click.style(
#             f"(iteration: {iteration_counter}) Found {applen} appointments",
#             fg="green",
#             blink=True,
#         )
#     )
#
#     notification_message = ""
#
#     for appointment in appointments:
#         if duplicate_checker(appointment):
#             echo_appointment(appointment)
#             notification_message += f"{appointment.appointment_datetime} {appointment.doctor_name} ({rating.get(appointment.doctor_name, 'N/A')}) {appointment.clinic_name} ({appointment.specialization_name})" +(" (Telefonicznie)\n" if appointment.is_phone_consultation else " (Stacjonarnie)\n")
#
#     if notification_message:
#         notification_title = kwargs.get("notification_title")
#         notify_external_device(
#             notification_message, notifier, notification_title=notification_title
#         )
#
#
# def echo_appointment(appointment):
#     click.echo(
#         appointment.appointment_datetime
#         + " "
#         + click.style(appointment.doctor_name + " (" + rating.get(appointment.doctor_name, 'N/A') + ")", fg="bright_green")
#         + " "
#         + appointment.clinic_name
#         + f" ({appointment.specialization_name}) "
#         + ("(Telefonicznie)" if appointment.is_phone_consultation else "(Stacjonarnie)")
#     )
#
#
# def validate_arguments(**kwargs) -> bool:
#     if kwargs["service"] == -1 and kwargs["bookingtype"] == 1:
#         click.echo("Service is required when bookingtype=1 (Diagnostic procedure)")
#         return False
#
#     if kwargs["specialization"] == -1 and kwargs["bookingtype"] == 2:
#         click.echo("Specialization is required when bookingtype=2 (Consulting)")
#         return False
#     return True
#
#
# @click.command()
# @click.option("--region", "-r", required=True, show_default=True)
# @click.option("--bookingtype", "-b", default=2, show_default=True)
# @click.option("--specialization", "-s", default=-1)
# @click.option("--clinic", "-c", default=-1)
# @click.option("--doctor", "-o", default=-1)
# @click.option("--start-date", "-d", default=now_formatted, show_default=True)
# @click.option("--end-date", "-f")
# @click.option("--start-time", "-a", default="0:00", show_default=True)
# @click.option("--end-time", "-g", default="23:59", show_default=True)
# @click.option("--service", "-e", default=-1)
# @click.option("--interval", "-i", default=0.0, show_default=True)
# @click.option("--days-ahead", "-j", default=1, show_default=True)
# @click.option("--enable-notifier", "-n", type=click.Choice(["pushover", "telegram", "xmpp"]))
# @click.option("--notification-title", "-t")
# @click.option("--user", prompt=True)
# @click.password_option(confirmation_prompt=False)
# @click.option("--disable-phone-search", is_flag=True)
# def find_appointment(
#     user,
#     password,
#     region,
#     bookingtype,
#     specialization,
#     clinic,
#     doctor,
#     start_date,
#     end_date,
#     start_time,
#     end_time,
#     service,
#     interval,
#     days_ahead,
#     enable_notifier,
#     notification_title,
#     disable_phone_search,
# ):
#
#     if end_date:
#         start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
#         end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
#         diff = end_date_dt - start_date_dt
#         days_ahead = diff.days
#
#     valid = validate_arguments(
#         bookingtype=bookingtype, specialization=specialization, service=service
#     )
#
#     if not valid:
#         return
#
#     iteration_counter = 1
#     med_session = MedicoverSession(username=user, password=password)
#
#     try:
#         med_session.log_in()
#     except Exception:
#         click.secho("Unsuccessful logging in", fg="red")
#         return
#
#     click.echo("Logged in")
#
#     med_session.load_search_form()
#
#     while interval > 0 or iteration_counter < 2:
#         appointments = []
#         start_date_param = start_date
#         for _ in range(days_ahead):
#             found_appointments = med_session.search_appointments(
#                 region=region,
#                 bookingtype=bookingtype,
#                 specialization=specialization,
#                 clinic=clinic,
#                 doctor=doctor,
#                 start_date=start_date_param,
#                 end_date=end_date,
#                 start_time=start_time,
#                 end_time=end_time,
#                 service=service,
#                 disable_phone_search=disable_phone_search
#             )
#
#             if not found_appointments:
#                 break
#
#             appointment_datetime = found_appointments[-1].appointment_datetime
#             appointment_datetime = datetime.strptime(
#                 appointment_datetime, "%Y-%m-%dT%H:%M:%S"
#             )
#             appointment_datetime = appointment_datetime + timedelta(days=1)
#             start_date_param = appointment_datetime.date().isoformat()
#             appointments.extend(found_appointments)
#
#         if not appointments:
#             click.echo(
#                 click.style(
#                     f"(iteration: {iteration_counter}) No results found", fg="yellow"
#                 )
#             )
#         else:
#             process_appointments(
#                 appointments,
#                 iteration_counter,
#                 notifier=enable_notifier,
#                 notification_title=notification_title,
#             )
#
#         iteration_counter += 1
#         time.sleep(interval * 60)
#
#
# FIELD_NAMES = ["specialization", "region", "clinic", "doctor"]
#
#
# @click.command()
# @click.option(
#     "-f", "--field-name", type=click.Choice(FIELD_NAMES), default="specialization"
# )
# def show_params(field_name):
#     params = load_available_search_params(field_name)
#     for p in params:
#         text = p["text"]
#         id_ = p["id"]
#         print(f" {text} (id={id_})")
#
#
# @click.command()
# @click.option("--user", prompt=True)
# @click.password_option(confirmation_prompt=False)
# def my_plan(user, password):
#     med_session = MedicoverSession(username=user, password=password)
#     try:
#         med_session.log_in()
#     except Exception:
#         click.secho("Unsuccessful logging in", fg="red")
#         return
#     click.echo("Logged in")
#     plan = med_session.get_plan()
#
#     with open("plan.tsv", mode="wt", encoding="utf-8") as f:
#         f.write(plan)
#
#
# @click.command()
# @click.option("--user", prompt=True)
# @click.password_option(confirmation_prompt=False)
# def my_appointments(user, password):
#     med_session = MedicoverSession(username=user, password=password)
#     try:
#         med_session.log_in()
#     except Exception:
#         click.secho("Unsuccessful logging in", fg="red")
#         return
#     click.echo("Logged in")
#     appointments = med_session.get_appointments()
#
#     planned_appointments = list(filter(lambda a: datetime.strptime(
#         a.appointment_datetime, "%Y-%m-%dT%H:%M:%S"
#     ) >= now, appointments))
#     if planned_appointments:
#         click.echo("Showing only planned appointments:")
#         for planned_appointment in planned_appointments:
#             echo_appointment(planned_appointment)
#     else:
#         click.echo("No planned appointments.")
#
#
#
# @click.command()
# def server():
#     print("BAM!")
#
#
# @click.group()
# def medihunter():
#     pass
#
#
# medihunter.add_command(show_params)
# medihunter.add_command(find_appointment)
# medihunter.add_command(my_plan)
# medihunter.add_command(my_appointments)
# medihunter.add_command(server)
#
#
# if __name__ == "__main__":
#     serve()
#     # medihunter()
