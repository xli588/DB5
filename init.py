from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

### main page ###
@app.route("/")
def Welcome():
    return render_template('Welcome.html')

@app.route("/Staff")
def Staff():
    return render_template('Staff.html')

@app.route("/Guest")
def Guest():
    return render_template('Guest.html')

### level 1 ###
@app.route("/Movie")
def Movie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Movie")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('Movie.html',users=users)


@app.route("/Genre")

def Genre():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from Genre")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('Genre.html',users=users)


@app.route("/Showing")

def Showing():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from Showing")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('Showing.html',users=users)


@app.route("/Customer")

def Customer():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from Customer")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('Customer.html',users=users)


@app.route("/Attend")

def Attend():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from Attend")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('Attend.html',users=users)

@app.route("/TheatreRoom")

def TheatreRoom():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from TheatreRoom")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('TheatreRoom.html',users=users)

### level 2 Movie ###

@app.route('/enterMoviename')
def MovieName(name=None):
    return render_template('formMovie.html', name=name)

@app.route('/Moviesubmit', methods=["POST"])
def Moviesubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Movie ( MovieName, MovieYear) "
        "VALUES (%s, %s)"
    )
    data = ( request.form['moviename'], request.form['movieyear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexMovie.html', moviename=request.form['moviename'], movieyear=request.form['movieyear'])


@app.route('/sqlInjection')
def sqlInjection(name=None):
    return render_template('form2Movie.html')

@app.route('/submitSqlInjection', methods=["POST"])
def sqlInjectionResult():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    firstName = request.form['firstname']
    query = ("SELECT * from Customer where firstname = '" + firstName + "'")
    cursor.execute(query)
    print("Attempting: " + query)
    users=cursor.fetchall()

    cnx.commit()
    cnx.close()
    return str(users)


### level 2 Customer ###
@app.route('/enterCustomername')
def CustomerName(name=None):
    return render_template('formCustomer.html', name=name)

@app.route('/Customersubmit', methods=["POST"])
def Customersubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Customer ( FirstName, LastName, Email, Sex) "
        "VALUES ( %s, %s, %s, %s)"
    )
    data = (request.form['firstname'], request.form['lastname'], request.form['email'], request.form['sex'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexCustomer.html', firstname=request.form['firstname'], lastname=request.form['lastname'], email=request.form['email'], sex=request.form['sex'])

### level 2 Genre ###
@app.route('/enterGenrename')
def GenreName(name=None):
    return render_template('formGenre.html', name=name)

@app.route('/Genresubmit', methods=["POST"])
def Genresubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Genre (Genre,  Movie_idMovie) "
        "VALUES (%s, %s)"
    )
    data = ( request.form['genre'], request.form['movieid'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexGenre.html', genre=request.form['genre'], movieid=request.form['movieid'])

### level 2 Attend ###
@app.route('/enterAttendname')
def AttendName(name=None):
    return render_template('formAttend.html', name=name)

@app.route('/Attendsubmit', methods=["POST"])
def Attendsubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Attend (CustomerID, ShowingID, Rating) "
        "VALUES (%s, %s, %s)"
    )
    data = ( request.form['customerid'], request.form['showingid'], request.form['rating'] )
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexAttend.html', customerid=request.form['moviename'])

### level 2 Showing ###
@app.route('/enterShowingname')
def ShowingName(name=None):
    return render_template('formShowing.html', name=name)

@app.route('/Showingsubmit', methods=["POST"])
def Showingsubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Showing ( ShowingID, ShowingDateTime, MovieID, RoomNumber, TicketPrice) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    data = ( request.form['moviename'], request.form['movieyear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexShowing.html')

### level 2 TheatreRoom ###
@app.route('/enterTheatreRoomname')
def TheatreRoomName(name=None):
    return render_template('formTheatreRoom.html', name=name)

@app.route('/TheatreRoomsubmit', methods=["POST"])
def TheatreRoomsubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO TheatreRoom (RoomNumer, Capacity) "
        "VALUES (%s, %s"
    )
    data = ( request.form['moviename'], request.form['movieyear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexTheatreRoom.html', moviename=request.form['moviename'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)