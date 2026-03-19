from imageai.Classification import ImageClassification
import os


execution_path = os.getcwd()


prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2-b0353104.pth"))
prediction.loadModel()
prediction.useCPU()


predictions, probabilities = prediction.classifyImage(
    os.path.join(execution_path, "020 giraffe.jpg"), result_count=10
)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
