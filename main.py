print("STARTING PROGRAM")
from model import predict_performance

print("🎓 Student Performance Predictor")

study = float(input("Enter study hours: "))
attendance = float(input("Enter attendance (%): "))
sleep = float(input("Enter sleep hours: "))

result = predict_performance(study, attendance, sleep)

print("Predicted Performance:", result)