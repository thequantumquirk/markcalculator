from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        
        # Reciving 10th Marks from the form

        tenth_tamil=request.form['tenth_tamil']
        tenth_english=request.form['tenth_english']
        tenth_maths=request.form['tenth_maths']
        tenth_science=request.form['tenth_science']
        tenth_social=request.form['tenth_social']

        # Making a List and finding Top 3 Marks

        list_of_tenth= [tenth_tamil,tenth_english,tenth_maths,tenth_science,tenth_social]
        (first_tenth)=max(list_of_tenth)
        list_of_tenth.remove(first_tenth)
        (second_tenth)=max(list_of_tenth)
        list_of_tenth.remove(second_tenth)
        (third_tenth)=max(list_of_tenth)
        
        # Calculating tenth Marks according to TN Marking Scheme

        tenth_mark=((int(first_tenth)+int(second_tenth)+int(third_tenth))/3)/2

        # Reciving 11th Marks from the form
        ele_tamil=request.form['ele_tamil']
        ele_english=request.form['ele_english']
        ele_maths=request.form['ele_maths']
        ele_physics=request.form['ele_physics']
        ele_chemistry=request.form['ele_chemistry']
        ele_cs=request.form['ele_cs']
        
        # Calculating ele Marks according to TN Marking Scheme
        ele_tamil = ((int(ele_tamil)-10)/90)*20
        ele_english = ((int(ele_english)-10)/90)*20
        ele_maths = ((int(ele_maths)-10)/90)*20
        ele_physics = ((int(ele_physics)-30)/70)*20
        ele_chemistry = ((int(ele_chemistry)-30)/70)*20
        ele_cs = ((int(ele_cs)-30)/70)*20
        
        # Calculating 12th Marks according to TN Marking Scheme
        twel_tamil = tenth_mark + ele_tamil + 30
        twel_english = tenth_mark + ele_english + 30
        twel_maths = tenth_mark + ele_maths + 30
        twel_physics = tenth_mark + ele_physics + 30
        twel_chemistry = tenth_mark + ele_chemistry + 30
        twel_cs = tenth_mark + ele_cs + 30
        sum= twel_tamil+twel_english+twel_chemistry+twel_physics+twel_maths+twel_cs
        return render_template('app.html', sum=int(sum))

if __name__ == ' __main__':
    app.debug = True
    app.run()
