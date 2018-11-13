#!/usr/bin/env python
# coding=utf-8
a = "admission_time=&years=&native_place_province_exclude=edi3W6UgeQ8_c&school_province_code=&longitude=O_bHhq2k2J4SD_b1r0idvSbw_c_c&latitude=jEzkB33FsdZ6CccMw2ZEag_c_c&version=ElF_aHf5fcoE_c&school_id=&login_token=sncrDH_aTuai_bZIHKb8GaASvXTqPBibA_bQlSc1qw8sGV6CccMw2ZEag_c_c&uid=rYzfkb6EjWQ_c&device=kDKb93msreCFRm9iFURUDyTkf2q3sLomkheybDmeacS4r014C5saHw_c_c&safe_code=YEo5sKEnyXwOam5akzneBVYTuN2Vrk7xVwQwsLfUvKB6CccMw2ZEag_c_c&chinese_zodiac_list=&v=k24nP4uRE2w_c&uuid=b2Sf_b3_a0nKhEMOMQ_bj_aN6pKGT_b15wjgfWcbV2_adVUMB6CccMw2ZEag_c_c&major_id=&skey=_aCKsz8R4a_a8dMvbrWAX5wGvrb_aJnaIkiegnHDMNmRGo_c&action=apnQ1zqR0VH2_aMeiEnFuyg_c_c&before_uuid=AIgGG3jBN7Sxw3Y1hF48MRY8HRgmwwljOm3LF5kLYcB6CccMw2ZEag_c_c&native_place_province_code=&sex=&degree=&time=5MdGX714_bBGBWkpVndHkCg_c_c&constellation_list="
ab = a.split("&")
body = {}
for k in ab:
    km = k.split("=")
    body[km[0]] = km[1]
print(body)