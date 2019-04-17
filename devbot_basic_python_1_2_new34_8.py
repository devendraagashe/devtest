import pandas as pd
from pprint import PrettyPrinter
from virtassnt.core import Node, Message

df = pd.read_csv(r"/home/ANANT/djaisinghani/doc_bot/dagserver/bots/testdata")

class CustomAction_sales_trend_custom_action(Node):

	def __init__(self, name):
		self.pprint = PrettyPrinter(indent=4)
		super(CustomAction_sales_trend_custom_action, self).__init__(name)


	def call(self, incoming_msg):
		data=incoming_msg.data
		entities = data["entities"]
		print(entities)
		geography_data = entities["geography"].upper()
		print(geography_data)
		product_data = entities["product"]
		print(product_data)
		metric_data = entities["metric"]
		print(metric_data)
		time_period_data = entities["time_period"]
		print(time_period_data)
		intent_data = "sales_trend"
		print(intent_data)
		
		df2 = df[(df['geography'] == geography_data) & (df['product'] == product_data) & (df['metric'] == metric_data) & (df['time_period'] == time_period_data) & (df['intent'] == intent_data)]
		df1 = df2[['metric_value','week_date']]
		print(df1)
		testout = df1.values
		print(testout)
		data = []
		for res in testout:
					data.append({'WEEK':res[1],'METRIC':res[0]})
					print(data)
				
		results = {
            "for_response": {
                "results": {
                    "type":	"table",
					"title":	"Sales Trend Data",
                    "data":	data,
                }
            }
        }
		outgoing_msg=Message.merge([incoming_msg, Message(results)])
		return super(CustomAction_sales_trend_custom_action, self).call(outgoing_msg)
		
class CustomAction_patient_trend_custom_action(Node):

	def __init__(self, name):
		self.pprint = PrettyPrinter(indent=4)
		super(CustomAction_patient_trend_custom_action, self).__init__(name)


	def call(self, incoming_msg):
		data=incoming_msg.data
		entities = data["entities"]
		print(entities)
		geography_data = entities["geography"].upper()
		print(geography_data)
		product_data = entities["product"]
		print(product_data)
		metric_data = entities["metric"]
		print(metric_data)
		time_period_data = entities["time_period"]
		print(time_period_data)
		intent_data = "patient_trend"
		print(intent_data)
		
		df2 = df[(df['geography'] == geography_data) & (df['product'] == product_data) & (df['metric'] == metric_data) & (df['time_period'] == time_period_data) & (df['intent'] == intent_data)]
		df1 = df2[['metric_value','week_date']]
		print(df1)
		testout = df1.values
		print(testout)
		data = []
		for res in testout:
					data.append({'WEEK':res[1],'METRIC':res[0]})
					print(data)
		results = {
            "for_response": {
                "results": {
                    "type":	"table",
					"title":	"Patient Trend Data",
                    "data":	data,
                }
            }
        }
		outgoing_msg=Message.merge([incoming_msg, Message(results)])
		return super(CustomAction_patient_trend_custom_action, self).call(outgoing_msg)

class CustomAction_call_activity_custom_action(Node):

	def __init__(self, name):
		self.pprint = PrettyPrinter(indent=4)
		super(CustomAction_call_activity_custom_action, self).__init__(name)


	def call(self, incoming_msg):
		data=incoming_msg.data
		entities = data["entities"]
		print(entities)
		geography_data = entities["geography"].upper()
		print(geography_data)
		product_data = entities["product"]
		print(product_data)
		metric_data = entities["metric"]
		print(metric_data)
		time_period_data = entities["time_period"]
		print(time_period_data)
		intent_data = "call_activity"
		print(intent_data)
		
		df2 = df[(df['geography'] == geography_data) & (df['product'] == product_data) & (df['metric'] == metric_data) & (df['time_period'] == time_period_data) & (df['intent'] == intent_data)]
		df1 = df2[['metric_value','week_date']]
		print(df1)
		testout = df1.values
		print(testout)
		data = []
		for res in testout:
					data.append({'WEEK':res[1],'METRIC':res[0]})
					print(data)
				
		results = {
            "for_response": {
                "results": {
                    "type":	"table",
					"title":	"Call Activity Data",
                    "data":	data,
                }
            }
        }
		outgoing_msg=Message.merge([incoming_msg, Message(results)])
		return super(CustomAction_call_activity_custom_action, self).call(outgoing_msg)

class CustomAction_competitor_sales_custom_action(Node):

	def __init__(self, name):
		self.pprint = PrettyPrinter(indent=4)
		super(CustomAction_competitor_sales_custom_action, self).__init__(name)


	def call(self, incoming_msg):
		data=incoming_msg.data
		entities = data["entities"]
		print(entities)
		geography_data = entities["geography"].upper()
		print(geography_data)
		product_data = entities["product"]
		print(product_data)
		metric_data = entities["metric"]
		print(metric_data)
		time_period_data = entities["time_period"]
		print(time_period_data)
		intent_data = "competitor_sales"
		print(intent_data)
		
		df2 = df[(df['geography'] == geography_data) & (df['product'] == product_data) & (df['metric'] == metric_data) & (df['time_period'] == time_period_data) & (df['intent'] == intent_data)]
		df1 = df2[['metric_value','week_date']]
		print(df1)
		testout = df1.values
		print(testout)
		data = []
		for res in testout:
					data.append({'WEEK':res[1],'METRIC':res[0]})
					print(data)
				
		results = {
            "for_response": {
                "results": {
                    "type":	"table",
					"title":	"Competitor Sales Data",
                    "data":	data,
                }
            }
        }
		outgoing_msg=Message.merge([incoming_msg, Message(results)])
		return super(CustomAction_competitor_sales_custom_action, self).call(outgoing_msg)
