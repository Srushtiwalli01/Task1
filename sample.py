import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_files(directory):
    files = [file for file in os.listdir(directory) if file.endswith('.txt')]
    notes = [open(os.path.join(directory, file), encoding='utf-8').read() for file in files]
    return files, notes

def vectorize(texts):
    vectorizer = CountVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()
    return vectors

def calculate_similarity(vectors):
    return cosine_similarity(vectors)

def check_plagiarism(files, vectors):
    plagiarism_results = set()

    for i in range(len(files)):
        for j in range(i+1, len(files)):
            sim_score = similarity_matrix[i][j]
            student_pair = sorted((files[i], files[j]))
            score = (student_pair[0], student_pair[1], sim_score)
            plagiarism_results.add(score)

    return plagiarism_results

directory = "."  # Change this to the directory containing your text files
student_files, student_notes = read_files(directory)
student_vectors = vectorize(student_notes)
similarity_matrix = calculate_similarity(student_vectors)
plagiarism_results = check_plagiarism(student_files, similarity_matrix)

for data in plagiarism_results:
    print(data)
