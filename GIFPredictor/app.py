from flask import Flask, request
from flask import render_template
import gif_predictor as gif
global output_final_gifs

app = Flask(__name__)
model, doc, order_centroids, terms = gif.model_trainer()
@app.route('/')
def hello_world():
    return render_template('blog.html')


@app.route('/hello_world2', methods=["GET", "POST"])
def hello_world2():
    user_input = request.form['user_input']
    id_keeper = []
    global output_final_gifs
    output_final_gifs, T, output_final_ids = gif.cluster_analysis(model,user_input, doc, order_centroids, terms)
    final_output = {}
    for gifs in output_final_gifs:
        final_output.update({gifs['id']: gifs['link']})
        id_keeper.append(gifs['id'])
    return render_template('blog2.html', output=final_output, id_keeper=id_keeper, gif_rows=output_final_gifs, T = T, output_final_ids = output_final_ids)

@app.route('/score_router', methods=["GET", "POST"])
def score_router():
    gif_id = request.form['vehicle']
    global output_final_gifs
    output = output_final_gifs
    T = request.form['T']
    output_final_ids = request.form['output_final_ids']
    gif.score_manipulator(output,gif_id,output_final_ids,T)
    print(gif_id)
    # with open('data_gifs_newest3.json', 'w') as outfile:
    #     json.dump(doc2, outfile)
    return render_template('blog.html')

if __name__ == '__main__':
    app.run()
