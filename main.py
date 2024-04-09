from typing import List, Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import joblib
from pydantic import BaseModel, Field
import numpy as np
import sklearn

app = FastAPI()

single_model = joblib.load(f'models/single_regression.joblib')
dual_model_1 = joblib.load(f'models/dual_regression_1.joblib')
dual_model_2 = joblib.load(f'models/dual_regression_2.joblib')
s1s2_model_1 = joblib.load(f'models/s1s2_regression_s1.joblib')
s1s2_model_2 = joblib.load(f'models/s1s2_regression_s2.joblib')

class SingleInputData(BaseModel):
    '''
    默认为中位数
    '''
    female_age: Optional[float] = Field(default=35., description="女方年龄")
    AFC: Optional[float] = Field(default=12., description="AFC")
    bFSH: Optional[float] = Field(default=5.63, description="bFSH")
    AMH: Optional[float] = Field(default=3.23, description="AMH")
    stimulation_protocol: Optional[float] = Field(default=1., description="促排方案")
    height: Optional[float] = Field(default=158.0, description="身高(cm)")
    weight: Optional[float] = Field(default=53.0, description="体重(kg)")
    BMI: Optional[float] = Field(default=20.96, description="BMI")
    bLH: Optional[float] = Field(default=3.205, description="bLH")
    E2: Optional[float] = Field(default=31., description="E2")
    FSH_LH: Optional[float] = Field(default=1.799004, description="FSH/LH")
    male_age: Optional[float] = Field(default=33, description="男方年龄")
    past_pregnancies: Optional[float] = Field(default=0., description="既往活产次数")
    total_oocytes: Optional[float] = Field(default=15., description="卵子总数")
    
class DualInputData(BaseModel):
    '''
    默认为中位数
    '''
    female_age: Optional[float] = Field(default=35., description="女方年龄")
    AFC: Optional[float] = Field(default=12., description="AFC")
    bFSH: Optional[float] = Field(default=5.63, description="bFSH")
    AMH: Optional[float] = Field(default=3.23, description="AMH")
    stimulation_protocol: Optional[float] = Field(default=1., description="促排方案")
    height: Optional[float] = Field(default=158.0, description="身高(cm)")
    weight: Optional[float] = Field(default=53.0, description="体重(kg)")
    BMI: Optional[float] = Field(default=20.96, description="BMI")
    bLH: Optional[float] = Field(default=3.205, description="bLH")
    E2: Optional[float] = Field(default=31., description="E2")
    FSH_LH: Optional[float] = Field(default=1.799004, description="FSH/LH")
    male_age: Optional[float] = Field(default=33, description="男方年龄")
    past_pregnancies: Optional[float] = Field(default=0., description="既往活产次数")
    
class S1S2InputData(BaseModel):
    '''
    默认为中位数
    '''
    female_age: Optional[float] = Field(default=35., description="女方年龄")
    AFC: Optional[float] = Field(default=12., description="AFC")
    bFSH: Optional[float] = Field(default=5.63, description="bFSH")
    AMH: Optional[float] = Field(default=3.23, description="AMH")
    stimulation_protocol: Optional[float] = Field(default=1., description="促排方案")
    height: Optional[float] = Field(default=158.0, description="身高(cm)")
    weight: Optional[float] = Field(default=53.0, description="体重(kg)")
    BMI: Optional[float] = Field(default=20.96, description="BMI")
    bLH: Optional[float] = Field(default=3.205, description="bLH")
    E2: Optional[float] = Field(default=31., description="E2")
    FSH_LH: Optional[float] = Field(default=1.799004, description="FSH/LH")
    male_age: Optional[float] = Field(default=33, description="男方年龄")
    past_pregnancies: Optional[float] = Field(default=0., description="既往活产次数")
    oocytes_transfer: Optional[float] = Field(default=1., description="可移植胚胎数")
    is_OHSS: Optional[float] = Field(default=0., description="是否中重度OHSS")
    total_oocytes_lt25: Optional[float] = Field(default=1., description="卵子总数是否≤25")

# 将静态文件目录映射到"/static"
app.mount("/static", StaticFiles(directory="static"), name="static")

# 首页路由
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    # 读取主页文件
    with open("static/index.html", "r") as file:
        content = file.read()
    return content

# 声明一个接受列表作为请求体的 POST API
@app.post("/api/single")
async def single(input_data: SingleInputData):
    input_list = [getattr(input_data, field) for field in  input_data.__fields__]
    input = np.array([input_list])
    output = single_model.predict(input)
    return {"output": f"{output[0]:.2f}"}

@app.post("/api/dual")
async def single(input_data: DualInputData):
    input_list = [getattr(input_data, field) for field in  input_data.__fields__]
    input = np.array([input_list])
    egg_num = dual_model_1.predict(input)
    sensiv = dual_model_2.predict(input)
    doses = egg_num[0] / sensiv[0]
    return {"nor": f"{egg_num[0]:.0f}",
            "fsh": f"{doses:.2f}"}
    
@app.post("/api/s1s2")
async def single(input_data: S1S2InputData):
    input_list = [getattr(input_data, field) for field in  input_data.__fields__]
    input = np.array([input_list])
    # 预测卵子总数
    total_eggs = s1s2_model_1.predict(input)
    total_eggs = np.round(total_eggs)
    input[0][13] = total_eggs[0]
    # 预测起始剂量
    does = s1s2_model_2.predict(input)
    return {"total_eggs": f"{total_eggs[0]:.0f}",
            "fsh":f"{does[0]:.2f}"}