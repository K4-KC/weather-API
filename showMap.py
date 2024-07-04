import requests
import numpy as np
import pygame
import pickle
from pathlib import Path
from datetime import datetime
import time
from threading import Thread

class CreateThread(Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def write_list(path, data):
    if path:
        with open(path, 'wb') as f:
            pickle.dump(data, f)

def loadingBar(percentage):
    percentage = percentage * 100
    if percentage == 0: return "[                    ]"
    elif percentage == 100: return "[====================]"
    else: return "[" + "="*int(percentage/5) + " "*(20-int(percentage/5)) + "]"

def get_temp(start_time, no, _lat_, _lon_, res, api_key):
    temp_array = np.empty(res)

    start_lat, end_lat = _lat_
    start_lon, end_lon = _lon_
    lat_step = (end_lat - start_lat) / res[0]
    lon_step = (end_lon - start_lon) / res[1]
    size = (res[0]) * (res[1])
    for i in range(res[0]):
        j, timed = 0, False
        while(j < res[1]):
            now = datetime.now()
            lat = round(end_lat - lat_step * i, 4)
            lon = round(start_lon + lon_step * j, 4)
            if not timed: print(now.strftime("%d%m%Y-%H%M%S-%f"), api_key, loadingBar((i*res[1]+(j+1))/size), 
                                '% 9.2f  %2d %3d:%-3d  % 6.2f:%- 7.2f'%(time.time()-start_time, no, i, j, lat, lon))
            url = BASE_URL + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key
            try:
                temp_array[i][j] = requests.get(url).json()['main']['temp']
                timed = False
                j += 1
            except:
                timed = True
                print(now.strftime("%d%m%Y-%H%M%S-%f"), api_key, loadingBar((i*res[1]+(j+1))/size), 
                      '% 9.2f  %2d %3d:%-3d  % 6.2f:%- 7.2f%23s%2d'%(time.time()-start_time, no, i, j, lat, lon, 'connection timed out ', no))
                continue

    return temp_array.tolist()

def mergeColors(color1, color2, ratio):
    return (color1[0]*ratio+color2[0]*(1-ratio), color1[1]*ratio+color2[1]*(1-ratio), color1[2]*ratio+color2[2]*(1-ratio))

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?lat="
API_KEY = ["77870069d2447b79ae6c8f9cc771849b",
           "28271809eb874b2c8c754b550fdd5c33",
           "7edd7f087fd25a7c25885ffdd70b9cfd",
           "a8668c54d344cb31bef9ce7093d69fab",
           "9ec0b398e350cc61db684d7ff6d77b69",
           "623b30bc49715adb3455fc2e48bac524",
           "cc3a87e2ba5dd6638e5122f0cbb9cddb",
           "167c2ca3a4a12671e30ba4a01815e988",
           "2f0fc2a200703f5b747879b27821d8b5",
           "ce776815984cad63aaf562706c942282",
           "1aa4ac0bf96751229e6502b8d296a808",
           "d7fd2a3e3a24aba03e419137c6a4e80d",
           "63618572cf6513f7dc33072e057599df",
           "5294c35c77731b7465619bb8206258b3",
           "fb1fb23fe0cb0bd299e47cb210a0fd84",
           "dca054c8b1c5e25cea7ab49cfedb5e8b",
           "d4a466b4be0c3e9e7c5bae2b122c9c94",
           "76d962906db38cfdf9ca6c8c8e58c981",
           "41e9e0582e8adedd275afac51f74e8d9",
           "0ea9b51b28ec57da18285b02c625dbff",
           "993e0785e1caaa01620c993b0110fa72",
           "09603f0915b34eaa644656da0950f4d5",
           "8bc6dae96cd64b06d851f1a01c39c71c",
           "f51c8ed2570ba898b788aa0d5825e891",
           "49694462da557ba79481be3d73e1775e",
           "83c74b3ab2497f4b039fcf336bb2ba19",
           "b67f7901863d91faea5660ae3a340472",
           "468a2de0a5957400f7b6f6c198f27fea",
           "9b622fb7c0d0eedb7d43ff2bf3108f2f",
           "afb16ac8cf897c0ad149ee8eaa0a55dc",
           "bf1614dd47ba78fa2f570d9b7fe84914",
           "a2c3f55a73e2a51e374b3ae45315aba6",
           "a664d31cfd1272bf56a6cad11ac7cb49",
           "47967dc79f2dd8411a44f1aff0449534",
           "54bfab673fe3deabd7c4163aa7357311",
           "cf6ad79fcae0b6ec6bc46fc851b0d88a",
           "5809a6036068c0e2fa28d8f5aece4fcf",
           "7580bfd01de3f8ef4dafd21883e5cbfe",
           "10b7915a0c90c73dd49840ce53a934a1",
           "99e3c6b354b58c3d3f2ac2ccb5886a60",
           "2900456308f30f72e7e1f699e6620ba6",
           "9faea4d5608c9868ca8e0ffa4edd2595",
           "733cc44a1aa157a3c800fda0af14f1d3",
           "7cd5b76d36bfc3205ce49f581b8fd5ba",
           "5fbbbf7b9c7b2a8f40db138a6229b603",
           "5508fae8a880a40430006d95641cd3bb",
           "6748eaaf96cbc567058b14a8f8e4aca7",
           "6b7c0e1ec2c386bf472f869de3c17a4f",
           "769eb60d695cb6dc36c91df1ccc2d8c0",
           "a1b0d5c20fd5f333cb6d0c66a0b8cd76",
           "2b6892e295f04bc508f1f2f9678074ed",
           "e51df7cbfd8244ccf02a2565461dbc47",
           "b12d0ce4215ddbb27a154dcb64c33e61",
           "fab97639f50fa59ff6500481d8dbc3d3",
           "82f427e0d00a6c1bd940fbc715ee2ad1",
           "10237d2833e0329a9e2f65e57cf65c4c",
           "30a034a89424ea4910ae045e0d4e37ad",
           "e1bec2696cda4e9fa119316641d72f3d",
           "18bc33266bbcf74ff93c8fdc33690cba",
           "7f3a11a16dc597469cc2538a8e96cf04",
           "7e92f431747971823263ab4213f7099a",
           "a71004a73c0c084d49e4effdd7156aa1",
           "27ec09bbc463e778843dee82b2f52852",
           "d2147da99f8e36dcb2cd1e745ddd2615",
           "ca9b5ddc4fc86581bf9bf7b8070a0b1f",
           "a9435a69186c80fc51a4f69716e2ead7",
           "21cc072cc85ff0dffe91f879baedfec1",
           "9c84ac5773f3ccacbe0dfc1ebeed0f55",
           "af5a55e51428a8f7a358bb4edee3dde7",
           "c8d4c71cfe3ff8c4aa50eed2dbf901b6",
           "88aeff0fb849b6558c6e467eba6c688c"]


file_path = "C:/Users/kanva/Desktop/rave unde/temp_list_southamerica_420x316_-55-14_-85--33.txt"

start_lat, end_lat = -55, 14
start_lon, end_lon = -85, -33
# res = (120, int((start_lon-end_lon)/(start_lat-end_lat)*120))
res = (420, 316)
print(res)

threadNo = 70
threads = [None]*threadNo
for i in range(threadNo):
    threads[i] = CreateThread(target=get_temp, args=(time.time(), i, 
        (end_lat-(i+1)*(end_lat-start_lat)/threadNo, end_lat-i*(end_lat-start_lat)/threadNo), 
            (start_lon, end_lon), (res[0]//threadNo, res[1]), API_KEY[i]))
    threads[i].start()

temp_list = []
for i in range(threadNo):
    for join in threads[i].join():
        temp_list.append(join)
    print("Thread", i, "done")
write_list(file_path, temp_list)
print("List written in ", file_path)



# temp_data = Path(file_path)

# with temp_data.open('rb') as f:
#     temp_data = pickle.load(f)

# # temp_temp = []
# # for j in range(20):
# #     for i in range(7):
# #         temp_temp.append(temp_data[(j+1)*7-i-1])

# temp_array = np.array(temp_data)
# print(temp_array.shape)

# pygame.init()

# res = temp_array.shape
# window_res = (300, 300)
# screen = pygame.display.set_mode(window_res)
# temp_surface = pygame.Surface((res[1], res[0]), pygame.SRCALPHA)

# # short_temp_array = np.array(temp_array[:10, :10])
# # MAX_TEMP = np.max(short_temp_array)
# # MIN_TEMP = np.min(short_temp_array)

# colors = ((255, 197, 20), (0, 17, 232))

# MAX_TEMP = np.max(temp_array)
# MIN_TEMP = np.min(temp_array)
# division = (MAX_TEMP - MIN_TEMP)
# print(MAX_TEMP, MIN_TEMP, division)

# running = True
# while(running):
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
        
#     for i in range(res[1]):
#         for j in range(res[0]):
#             temp = temp_array[j][i]
#             temp = (temp - MIN_TEMP)/division
#             temp_surface.set_at((i, j), mergeColors(colors[0], colors[1], temp))

#     screen.blit(temp_surface, ((window_res[0]-res[1])//2, (window_res[1]-res[0])//2))

#     pygame.display.flip()