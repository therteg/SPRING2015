import logging
import motor
import settings

client = motor.MotorClient('localhost', 27017)
db = client.test2_database