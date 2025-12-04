#This function get a data and save the report

def select_month (months) : 

    input_of_the_month = input("Ingrese el mes del informe: ")

    while not input_of_the_month in months : 

        input_of_the_month = input("Ingrese el mes del informe: ")
    
    return input_of_the_month

#This function get reports and save

def data_entry_of_reports (group_5)  :

    total_members = []

    for members in range(len(group_5)) : 

        member = group_5[members]
        input_of_the_activity = input(f"¿Ha realizado actividad el hno / hna {member}?: ")
        total_members.append(input_of_the_activity)
    
    return total_members


def special_reports (regulars_precursors, auxiliar_precursors, group_5) :

    regular_report = []
    auxiliar_report = []

    for members in range(len(group_5)) : 

        member = group_5[members]

        if member in regulars_precursors or member in auxiliar_precursors: 

            input_of_the_hours = int(input(f"Ingrese las horas realizadas como precursor de {member}: "))
            regular = f'{member} = {input_of_the_hours}'
            regular_report.append(regular)

    return regular_report, auxiliar_report

#This function show all of the members

def show_participants_and_reports (group_5, reports) : 
    
    general_list = []
    index = 0

    while index < len(group_5) - 1 : 

        members_and_reports = (group_5[index], reports[index])
        general_list.append(members_and_reports)
        index = index + 1
    
    return general_list

#MAIN

group_5 = ['Arteaga Bedoya Eva', 'Bedoya Callejas Eva', 'Domínguez Juan',
            'Domínguez Miriam', 'Domínguez Patricio', 'Encina Gerardo', 
            'Encina Mónica', 'Gonchay Alejandro', 'Gonchay Brenda', 
            'Gonchay Ema', 'Morales Nahiara', 'Morales Ramona',
            'Ovejero Gustavo', 'Viera Alex', 'Viera Cristian',
            'Viera Valeria']

auxiliar_precursors = ['Juan Domínguez']
regular_precursors = ['Encina Gerardo', 'Encina Mónica']

total_months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


month_selected = select_month(total_months)
input_of_the_data = data_entry_of_reports(group_5)
reports_with_hours = special_reports(regular_precursors, auxiliar_precursors, group_5)
show_members = show_participants_and_reports(group_5, input_of_the_data)

print(show_members)