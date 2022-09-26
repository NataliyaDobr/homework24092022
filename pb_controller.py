import pb_view
import pb_operation
import pb_model
import pb_input
import codecs
import pb_search

def button_click():
    v_tuple = pb_view.inpt()
    o_tuple = pb_operation.oper(v_tuple)
    if v_tuple[1]==2:
      pb_model.init(o_tuple[0], o_tuple[1],o_tuple[2],o_tuple[3])
      pb_input.write(o_tuple[0], o_tuple[1],o_tuple[2],o_tuple[3])
    elif v_tuple[1]==1:
      findnum = pb_search.serch_phone(o_tuple[0])
      pb_view.view_data(findnum)
