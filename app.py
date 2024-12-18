from flask import Flask, request, jsonify, make_response
from model import Data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def karyawan():
    dt = Data()
    values = ()

    if request.method == 'GET':
        id_ = request.args.get("id")
        if id_:
            query = "SELECT * FROM data_karyawan where id = %s "
            values = (id_,)
        else:
            query = "SELECT * FROM data_karyawan"
        data = dt.get_data(query, values)
        return make_response(jsonify(data), 200)

    elif request.method == 'POST':
        datainput = request.json
        nama = datainput['nama']
        pekerjaan = datainput['pekerjaan']
        usia = datainput['usia']
        
        query = "INSERT INTO data_karyawan (nama, pekerjaan, usia) values (%s,%s,%s) "
        values = (nama, pekerjaan, usia,)
        dt.insert_data(query, values) 
        data = [{
        'pesan': 'berhasil menambah data'
        }]
        return make_response(jsonify(data), 201)

    elif request.method == 'PUT':
        query = "UPDATE data_karyawan SET "
        id_ = request.args.get("id")
        datainput = request.json
        id_ = datainput['id']
        values = (id_,)
        update_query = []
        if 'nama' in datainput:
            nama = datainput['nama']
            values += (nama, )
            update_query.append("nama = %s")
        if 'pekerjaan' in datainput:
            pekerjaan = datainput['pekerjaan']
            values += (pekerjaan, )
            update_query.append("pekerjaan = %s")
        if 'usia' in datainput:
            usia = datainput['usia']
            values += (usia, )
            update_query.append("usia = %s")
        query += ", ".join(update_query)
        query += " where id = %s "
        values += (id_,)
        dt.insert_data(query, values) 
        data = [{
            'pesan': 'berhasil mengubah data'
        }]
        return make_response(jsonify(data), 200)

    else:
        query = "DELETE FROM data_karyawan where id = %s "
        id_ = request.args.get("id")
        values = (id_,)
        dt.insert_data(query, values) 
        data = [{
            'pesan': 'berhasil menghapus data'
        }]
    except Exception as e:
        return make_response(jsonify({'error' : str(e)}), 400)
    return make_response(jsonify(data), 200)

app.run()