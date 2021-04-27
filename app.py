from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Automapping the database into a new model
Base = automap_base()
# Reflecting the tables
Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

# Static routes only

@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    latest_date = dt.date(2017, 8, 23)
    year_range = latest_date - dt.timedelta(days=365)
    session = Session(engine)
    prcp_data = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year_range).all()
    session.close()
    date_prcp = {date: prcp for date, prcp in prcp_data}
    return jsonify(date_prcp)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_activity = session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    session.close()
    return jsonify(station_activity)

@app.route("/api/v1.0/tobs")
def tobs():
    latest_date = dt.date(2017, 8, 23)
    year_range = latest_date - dt.timedelta(days=365)
    session = Session(engine)
    station_activity = session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    active_id = station_activity[0][0]
    temps = session.query(measurement.date, measurement.tobs).filter(measurement.date >= year_range, measurement.station == active_id).all()
    session.close()
    return jsonify(temps)

if __name__ == "__main__":
    app.run(debug=True)