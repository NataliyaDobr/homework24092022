import pb_view
import pb_operation
import pb_model
import pb_input
import codecs

def button_click():
    v_tuple = pb_view.inpt()
    o_tuple = pb_operation.oper(v_tuple)
    pb_model.init(o_tuple[0], o_tuple[1],o_tuple[2],o_tuple[3])
    pb_input.write(o_tuple[0], o_tuple[1],o_tuple[2],o_tuple[3])
