import os
import requests
from pprint import PrettyPrinter
import json
from virtassnt.nodes import *
from virtassnt.core import Node, Message
from virtassnt.graph import Graph


class CustomAction_switch_details_custom_action(Node):

	def __init__(self, name):
		self.pprint = PrettyPrinter(indent=4)
		super(CustomAction_switch_details_custom_action, self).__init__(name)


	def call(self, incoming_msg):
		data=incoming_msg.data
		#Put API Logic Here

		results = {'for_response': results}
		outgoing_msg=Message.merge([incoming_msg, Message(results)])
		return super(CustomAction_switch_details_custom_action, self).call(outgoing_msg)

class CustomAction_brand_patient_count_custom_action(Node):

	def __init__(self, name):
		self.pprint = PrettyPrinter(indent=4)
		super(CustomAction_brand_patient_count_custom_action, self).__init__(name)


	def call(self, incoming_msg):
		data=incoming_msg.data
		#Put API Logic Here

		results = {'for_response': results}
		outgoing_msg=Message.merge([incoming_msg, Message(results)])
		return super(CustomAction_brand_patient_count_custom_action, self).call(outgoing_msg)

class CustomAction_switch_rx_fill_date_custom_action(Node):

	def __init__(self, name):
		self.pprint = PrettyPrinter(indent=4)
		super(CustomAction_switch_rx_fill_date_custom_action, self).__init__(name)


	def call(self, incoming_msg):
		data=incoming_msg.data
		#Put API Logic Here

		results = {'for_response': results}
		outgoing_msg=Message.merge([incoming_msg, Message(results)])
		return super(CustomAction_switch_rx_fill_date_custom_action, self).call(outgoing_msg)
def build_bot(user_id='anurag.kumar@saama.com'):

	graph=Graph(name='anurag.kumar@saama.com_gcva_dalia_tableau_poc_002', user_id=user_id)

	#Making the Nodes

	greet_user = Input('Hi. I am a bot. Tell me what you want to know.', text_only=True, name='greet_user')
	graph.add_node(greet_user)

	main_parser = NLUParser(name='main_parser', model_path='./main_parser', config_path='./resources/config_spacy.json')
	graph.add_node(main_parser)

	switch_details_master_validate = Validator(required_keys=['metric', 'metric_type'], name='switch_details_master_validate')
	graph.add_node(switch_details_master_validate)

	switch_details_metric_validate = Validator(required_keys=['metric'], name='switch_details_metric_validate')
	graph.add_node(switch_details_metric_validate)

	switch_details_metric_input = Input('Enter metric', text_only=True, name='switch_details_metric_input')
	graph.add_node(switch_details_metric_input)

	switch_details_metric_parse = NLUParser(name='switch_details_metric_parse', model_path='./switch_details_metric_parse', config_path='./resources/config_spacy.json')
	graph.add_node(switch_details_metric_parse)

	switch_details_metric_type_validate = Validator(required_keys=['metric_type'], name='switch_details_metric_type_validate')
	graph.add_node(switch_details_metric_type_validate)

	switch_details_metric_type_input = Input('Enter metric_type', text_only=True, name='switch_details_metric_type_input')
	graph.add_node(switch_details_metric_type_input)

	switch_details_metric_type_parse = NLUParser(name='switch_details_metric_type_parse', model_path='./switch_details_metric_type_parse', config_path='./resources/config_spacy.json')
	graph.add_node(switch_details_metric_type_parse)

	brand_patient_count_master_validate = Validator(required_keys=['metric', 'metric_type'], name='brand_patient_count_master_validate')
	graph.add_node(brand_patient_count_master_validate)

	brand_patient_count_metric_validate = Validator(required_keys=['metric'], name='brand_patient_count_metric_validate')
	graph.add_node(brand_patient_count_metric_validate)

	brand_patient_count_metric_input = Input('Enter metric', text_only=True, name='brand_patient_count_metric_input')
	graph.add_node(brand_patient_count_metric_input)

	brand_patient_count_metric_parse = NLUParser(name='brand_patient_count_metric_parse', model_path='./brand_patient_count_metric_parse', config_path='./resources/config_spacy.json')
	graph.add_node(brand_patient_count_metric_parse)

	brand_patient_count_metric_type_validate = Validator(required_keys=['metric_type'], name='brand_patient_count_metric_type_validate')
	graph.add_node(brand_patient_count_metric_type_validate)

	brand_patient_count_metric_type_input = Input('Enter metric_type', text_only=True, name='brand_patient_count_metric_type_input')
	graph.add_node(brand_patient_count_metric_type_input)

	brand_patient_count_metric_type_parse = NLUParser(name='brand_patient_count_metric_type_parse', model_path='./brand_patient_count_metric_type_parse', config_path='./resources/config_spacy.json')
	graph.add_node(brand_patient_count_metric_type_parse)

	switch_rx_fill_date_master_validate = Validator(required_keys=['metric', 'metric_type'], name='switch_rx_fill_date_master_validate')
	graph.add_node(switch_rx_fill_date_master_validate)

	switch_rx_fill_date_metric_validate = Validator(required_keys=['metric'], name='switch_rx_fill_date_metric_validate')
	graph.add_node(switch_rx_fill_date_metric_validate)

	switch_rx_fill_date_metric_input = Input('Enter metric', text_only=True, name='switch_rx_fill_date_metric_input')
	graph.add_node(switch_rx_fill_date_metric_input)

	switch_rx_fill_date_metric_parse = NLUParser(name='switch_rx_fill_date_metric_parse', model_path='./switch_rx_fill_date_metric_parse', config_path='./resources/config_spacy.json')
	graph.add_node(switch_rx_fill_date_metric_parse)

	switch_rx_fill_date_metric_type_validate = Validator(required_keys=['metric_type'], name='switch_rx_fill_date_metric_type_validate')
	graph.add_node(switch_rx_fill_date_metric_type_validate)

	switch_rx_fill_date_metric_type_input = Input('Enter metric_type', text_only=True, name='switch_rx_fill_date_metric_type_input')
	graph.add_node(switch_rx_fill_date_metric_type_input)

	switch_rx_fill_date_metric_type_parse = NLUParser(name='switch_rx_fill_date_metric_type_parse', model_path='./switch_rx_fill_date_metric_type_parse', config_path='./resources/config_spacy.json')
	graph.add_node(switch_rx_fill_date_metric_type_parse)

	switch_details_custom_action=CustomAction_switch_details_custom_action('switch_details_custom_action')
	graph.add_node(switch_details_custom_action)
	main_response = Response(name='main_response')
	main_response.add_response_pattern('[results]')
	graph.add_node(main_response)

	next_input = Input('Do you have any other question?', text_only=True, name='next_input')
	graph.add_node(next_input)

	brand_patient_count_custom_action=CustomAction_brand_patient_count_custom_action('brand_patient_count_custom_action')
	graph.add_node(brand_patient_count_custom_action)
	switch_rx_fill_date_custom_action=CustomAction_switch_rx_fill_date_custom_action('switch_rx_fill_date_custom_action')
	graph.add_node(switch_rx_fill_date_custom_action)
	end = End()
	graph.add_node(end)

	#Making the Connections

	greet_user.add_output(main_parser)
	main_parser.add_output('hi', greet_user)
	main_parser.add_output('bye', end)
	main_parser.add_output('switch_details', switch_details_master_validate)
	main_parser.add_output('brand_patient_count', brand_patient_count_master_validate)
	main_parser.add_output('switch_rx_fill_date', switch_rx_fill_date_master_validate)
	switch_details_master_validate.add_output(switch_details_custom_action, True)
	switch_details_master_validate.add_output(switch_details_metric_validate, False)
	switch_details_metric_validate.add_output(switch_details_metric_type_validate, True)
	switch_details_metric_validate.add_output(switch_details_metric_input, False)
	switch_details_metric_input.add_output(switch_details_metric_parse)
	switch_details_metric_parse.add_output('metric', switch_details_metric_validate)
	switch_details_metric_type_validate.add_output(switch_details_custom_action, True)
	switch_details_metric_type_validate.add_output(switch_details_metric_type_input, False)
	switch_details_metric_type_input.add_output(switch_details_metric_type_parse)
	switch_details_metric_type_parse.add_output('metric_type', switch_details_metric_type_validate)
	brand_patient_count_master_validate.add_output(brand_patient_count_custom_action, True)
	brand_patient_count_master_validate.add_output(brand_patient_count_metric_validate, False)
	brand_patient_count_metric_validate.add_output(brand_patient_count_metric_type_validate, True)
	brand_patient_count_metric_validate.add_output(brand_patient_count_metric_input, False)
	brand_patient_count_metric_input.add_output(brand_patient_count_metric_parse)
	brand_patient_count_metric_parse.add_output('metric', brand_patient_count_metric_validate)
	brand_patient_count_metric_type_validate.add_output(brand_patient_count_custom_action, True)
	brand_patient_count_metric_type_validate.add_output(brand_patient_count_metric_type_input, False)
	brand_patient_count_metric_type_input.add_output(brand_patient_count_metric_type_parse)
	brand_patient_count_metric_type_parse.add_output('metric_type', brand_patient_count_metric_type_validate)
	switch_rx_fill_date_master_validate.add_output(switch_rx_fill_date_custom_action, True)
	switch_rx_fill_date_master_validate.add_output(switch_rx_fill_date_metric_validate, False)
	switch_rx_fill_date_metric_validate.add_output(switch_rx_fill_date_metric_type_validate, True)
	switch_rx_fill_date_metric_validate.add_output(switch_rx_fill_date_metric_input, False)
	switch_rx_fill_date_metric_input.add_output(switch_rx_fill_date_metric_parse)
	switch_rx_fill_date_metric_parse.add_output('metric', switch_rx_fill_date_metric_validate)
	switch_rx_fill_date_metric_type_validate.add_output(switch_rx_fill_date_custom_action, True)
	switch_rx_fill_date_metric_type_validate.add_output(switch_rx_fill_date_metric_type_input, False)
	switch_rx_fill_date_metric_type_input.add_output(switch_rx_fill_date_metric_type_parse)
	switch_rx_fill_date_metric_type_parse.add_output('metric_type', switch_rx_fill_date_metric_type_validate)
	switch_details_custom_action.add_output(main_response)
	main_response.add_output(next_input)
	next_input.add_output(main_parser)
	brand_patient_count_custom_action.add_output(main_response)
	switch_rx_fill_date_custom_action.add_output(main_response)

	#Complete the Build
	graph.build_completed()
	return graph