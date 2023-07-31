from  parse_utils import parse_date
fname_personal = 'personal_info.csv'
fname_employement = 'employment.csv'
fname_vehicles = 'vehicles.csv'
fname_update_status= 'update_status.csv'

fnames = fname_personal,fname_employement,fname_vehicles,fname_update_status
#PARSERS
personal_parser = (str,str,str,str,str)
employement_parser = (str,str,str,str)
vehicles_parser =(str,str,str,int)
update_status_parser = (str,parse_date,parse_date)
parsers = personal_parser,employement_parser,vehicles_parser,update_status_parser

#Named Tuples
personal_class_name = 'Personal'
employement_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_status_class_name = 'UpdateStatus'
class_names = personal_class_name,employement_class_name,vehicle_class_name,update_status_class_name
personal_field_names = 'ssn','first_name','last_name','gender','langauge'

#FİELDS İNCLUSİON/EXCLUSİON
personal_fields_compress = [True,True,True,True,True]
employement_fields_compress = [True,True,True,False]
vehicle_fields_compress = [False,True,True,True]
update_status_fields_compress = [False,True,True]
compressed_fields = (personal_fields_compress,employement_fields_compress,vehicle_fields_compress,
                     update_status_fields_compress)
