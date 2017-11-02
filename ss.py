GLOBAL_VAL = {
                  "g_zuan_pt":"20150125000000",
                  "g_rank_pt":"20150125000000",
                  "g_cat_pt":"20160928000000",
                  "g_wish_cat_pt":"20160715000000",
                  "g_offer_rate":"20160508000000",
                  "v_item_dimt_pt":"",
                  }
a="g_cat_pt:20160928000000"
for p in a:
    print(p.split(":", 1))

if (a):                                        #设置全局变量
        for p in a:
            k, v = p.split(":", 1)
            if GLOBAL_VAL.has_key(k):
                msg = "The '%s' parameter is exists" % k
                raise  msg
            else:
                GLOBAL_VAL[k] = v