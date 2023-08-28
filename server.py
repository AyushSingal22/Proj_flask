
from flask import Flask, jsonify, render_template, request, send_file
import connection 

app = Flask(__name__)
data_provider = connection.Api_data_provider()
@app.route('/snowflake', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):
		query= request.args['q']
		data = data_provider.getData(str(query))
		return jsonify({'data': data})

@app.route('/vis', methods = ['GET', 'POST'])
def home2():
	if(request.method == 'GET'):
		query= request.args['q']
		data = data_provider.getData(str(query))
		bytes_obj=data_provider.data_vis(data)
		return send_file(bytes_obj,
                     mimetype='image/png')


@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):

	return jsonify({'data': num**2})

if __name__ == '__main__':

	app.run(debug = True)
