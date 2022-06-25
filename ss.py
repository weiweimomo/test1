from random import randrange

from flask import Flask, render_template,request,url_for

from pyecharts import options as opts
from pyecharts.charts import Bar


app = Flask(__name__)


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


@app.route("/")
def index():
    return render_template("index1.html")


@app.route("/barChart",methods=["post","get"])
def get_bar_chart():
    c = bar_base()
    n=request.values.get("name")
    print(n)
    return c.dump_options_with_quotes()


if __name__ == "__main__":

    app.run()