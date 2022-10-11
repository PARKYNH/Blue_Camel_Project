# 대한민국 전국 시, 도 지도에 표시해 보기
# 지도 그리기 참고 싸이트 (지도 다운로드, 통계청 정보 다운로드)
# https://blog.naver.com/PostView.nhn?blogId=kcchang61&logNo=221350672356

# %matplotlib inline

import numpy as np
import pandas as pd

import folium
import webbrowser
# import json

##import matplotlib as mpl
##import matplotlib.pyplot as plt
##import matplotlib.font_manager as fm
##from matplotlib import rc
### mpl.rcParams['axes.unicode_minus']=False

###############################################################    
# 목적: 대한민국 시, 도 지도에 정보 구분하여 색으로 표시해보기
# 예제 정보: 시도별 초등학생 / 초등교사 비율
###############################################################

def main():

    csvFile = 'Si_Do_Ele_students_Teacher_ratio.csv'
    SiDodf = pd.read_csv(csvFile, encoding = 'euc-kr')
    print(SiDodf)
    
    SiDo_geo = 'Si_Do_map_utf8.json'
    
    # Initialize the map at Daejeon 
    m = folium.Map(location=[36.45, 127.42], \
                   tiles="OpenStreetMap", zoom_start=8)

    # Json map polygon 경계좌표값으로 구역별 색칠하기 
    folium.Choropleth(
        geo_data = SiDo_geo,
        name='교원당 초등학생수',
        data=SiDodf,
        columns=['행정구역별', '초등생교원비'],
        key_on='feature.properties.CTP_KOR_NM',
        fill_color='PuRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='교원당 초등학생수').add_to(m)

    # 색칠한 layer 켜고 끄기 버튼 추가
    folium.LayerControl().add_to(m)
    
    m.save('map.html')
    webbrowser.open('map.html') 
    



# main 함수 로딩부
if __name__ == '__main__':
    main()
