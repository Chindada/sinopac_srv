# CHANGELOG

## Unreleased (2021-12-01)

### New feature

- **tse**: :memo: add tse lastcount and kbar([`46a51c2`](https://gitlab.tocraw.com/root/sinopac_srv/commit/46a51c2e9fddd213d29805a09e1a830a3cc31fbf)) (@TimHsu211104@DevContainer)
- **lastcount**: :pencil2: add multi date lastcount for biasrate([`0ccb179`](https://gitlab.tocraw.com/root/sinopac_srv/commit/0ccb179aa62b959703c4d60392d0792ed95efaa4)) (@TimHsu211104@DevContainer)
- **log**: :mute: modify place order callback message, set callback before login([`874f098`](https://gitlab.tocraw.com/root/sinopac_srv/commit/874f098f1266fbaf8fac184906b3880ee746a4bd)) (@TimHsu211104@DevContainer)
- **logger**: :monocle_face: add log json file, ci compress log files upload to gitlab([`f0dafb3`](https://gitlab.tocraw.com/root/sinopac_srv/commit/f0dafb3f1d5358f499b47f1e6971ad2d915512d4)) (@TimHsu211104@DevContainer)
- **ticktype**: :globe_with_meridians: add sinopac native tick_type in entiretick and tse_entiretick([`a3d4e46`](https://gitlab.tocraw.com/root/sinopac_srv/commit/a3d4e46a476dfa428a7dc35d66d98e2b5e45db16)) (@TimHsu211104@DevContainer)
- **shioaji**: :heavy_plus_sign: sinopac update to dev5([`d71d925`](https://gitlab.tocraw.com/root/sinopac_srv/commit/d71d92500b150d355ed32582d992f5ba1cba8427)) (@TimHsu211104@DevContainer)
- **ci**: :truck: change log file name and path([`26be410`](https://gitlab.tocraw.com/root/sinopac_srv/commit/26be410477e3a96ada108fa8c2a6b2eeef6e84f6)) (@TimHsu211104@DevContainer)
- **ci**: :boom: change logs path to root([`e96b0c2`](https://gitlab.tocraw.com/root/sinopac_srv/commit/e96b0c2597e5f4baea8e2470fce599455f99fba0)) (@TimHsu211104@DevContainer)

### Bugs fixed

- **ci**: :card_file_box: add mkdir -p /$SERVER_USER/sinopac_logs([`60c14ff`](https://gitlab.tocraw.com/root/sinopac_srv/commit/60c14ffab8c49544b659a3dc2068a2892ac1e3ad)) (@TimHsu211104@DevContainer)
- **fakedata**: :egg: remove fake data api, remove sinopac token error auto-pkill([`11f7d02`](https://gitlab.tocraw.com/root/sinopac_srv/commit/11f7d024c5791121c49098c5e38a1da8babc1079)) (@TimHsu211104@DevContainer)

## v1.5.0 (2021-11-08)

## v1.4.0 (2021-11-04)

### New feature

- **protobuf**: :zap: update to 3.19.1([`1f67d82`](https://gitlab.tocraw.com/root/sinopac_srv/commit/1f67d82370b9e4aa65e7b41cf59ac8f049e6e5fd)) (@TimHsu211103@DevContainer)

### Bugs fixed

- **logout**: :monocle_face: remove logout, update dependency, python up to 3.7.12([`b710aad`](https://gitlab.tocraw.com/root/sinopac_srv/commit/b710aadc50411b6d1f166150f3d4d72454436b9c)) (@TimHsu211104@DevContainer)

## v1.3.0 (2021-11-02)

### New feature

- **status**: :passport_control: add mutex for update status, move orders to global, if modified price exist, replace price([`285d92f`](https://gitlab.tocraw.com/root/sinopac_srv/commit/285d92fe96c5478bdc7549113e0e892a1ed8ec62)) (@TimHsu211028@DevContainer)
- **status**: :alien: add mutex for status([`e4285c4`](https://gitlab.tocraw.com/root/sinopac_srv/commit/e4285c47dbf3cbded27a08c7185adc4caa3b62be)) (@TimHsu211028@DevContainer)
- **healthcheck**: :alembic: add server token([`ac79551`](https://gitlab.tocraw.com/root/sinopac_srv/commit/ac79551d8358c816784ef5fa202b6f88592b709d)) (@TimHsu211028@DevContainer)

## v1.2.0 (2021-10-29)

### New feature

- **cancel**: :alien: add not found, already([`5ccd87a`](https://gitlab.tocraw.com/root/sinopac_srv/commit/5ccd87a6b5b476143d72eef05cdac3bd59e787b9)) (@TimHsu211014@DevContainer)
- **ca**: :camera_flash: activate ca once, change health up time to minute([`a6e4f3d`](https://gitlab.tocraw.com/root/sinopac_srv/commit/a6e4f3d22c6bece7c1c1070dc36c02167dde4b41)) (@TimHsu211014@DevContainer)
- **healthcheck**: :clown_face: add server up time for healthe check([`5768750`](https://gitlab.tocraw.com/root/sinopac_srv/commit/5768750600047e00e2e83b8a780d5f903232cc33)) (@TimHsu211014@DevContainer)
- **logout**: :building_construction: add logout, before request func, reconnect if request after logout([`8af65ac`](https://gitlab.tocraw.com/root/sinopac_srv/commit/8af65ac6e20980ef094b53f6bf4c115508a12dbc)) (@TimHsu211014@DevContainer)
- **kbar**: :speech_balloon: add kbar api([`b7088e5`](https://gitlab.tocraw.com/root/sinopac_srv/commit/b7088e5962c013fb6348dbd48eadaa54b0c55ede)) (@TimHsu211014@DevContainer)
- **kbar**: :truck: temp kbar, add date in volume rank([`3373549`](https://gitlab.tocraw.com/root/sinopac_srv/commit/3373549ff01ade9d09f7ce34c2d77c856f444c90)) (@TimHsu211014@DevContainer)
- **shiaoji**: :art: update to dev4, protocbuf to 3.18.1([`e1f1eb6`](https://gitlab.tocraw.com/root/sinopac_srv/commit/e1f1eb68de5eb34f7a7fd9e3d4a066e90234a5a7)) (@TimHsu@DevContainer)

### Bugs fixed

- **response**: :rotating_light: fix wrong response([`ce729ed`](https://gitlab.tocraw.com/root/sinopac_srv/commit/ce729ed24302fb693f9aaf49a5e4c4e5d04dcdc8)) (@TimHsu211028@DevContainer)
- **swagger**: :green_heart: health check wrong tag([`b5d1161`](https://gitlab.tocraw.com/root/sinopac_srv/commit/b5d1161ab9fa659b3c4e1ee38d62ddc71ca296af)) (@TimHsu211014@DevContainer)
- **jasonify**: :bug: check response is not empty, change log to json format([`68c7753`](https://gitlab.tocraw.com/root/sinopac_srv/commit/68c7753beecf9cf335d0cdbdfcd2fd7c1b372d0c)) (@TimHsu@DevContainer)

## v1.1.0 (2021-10-07)

### New feature

- **tse**: :clown_face: add tse tick, fix cancel fail([`2db724f`](https://gitlab.tocraw.com/root/sinopac_srv/commit/2db724fd85dc10909aeb63eecc0f31cddde30e67)) (@TimHsu@DevContainer)
- **trade**: :beers: add sell first api([`49f65bc`](https://gitlab.tocraw.com/root/sinopac_srv/commit/49f65bccde95c6d563f919743766203f0d38d501)) (@TimHsu@DevContainer)

## v1.0.0 (2021-09-28)

### New feature

- **ci**: :wrench: add docker logs as artifact([`9fa18d6`](https://gitlab.tocraw.com/root/sinopac_srv/commit/9fa18d646854278a5a64eb798c406c7d234121c7)) (@TimHsu@DevContainer)
- **future**: :loud_sound: add future sub, change login method, add mutex([`de5e23c`](https://gitlab.tocraw.com/root/sinopac_srv/commit/de5e23ca5aab4bf23fe4739285813c0dbdc7fe0a)) (@TimHsu@DevContainer)
