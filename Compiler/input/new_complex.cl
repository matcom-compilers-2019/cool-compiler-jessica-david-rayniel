class Main inherits IO {
    io : IO <- new Complex;
    main() : SELF_TYPE {
	(let c : Complex <- (new Complex).init(1, 1) in
	    {

	        --if ("david" = "davi") then out_string("bien") else out_string("mal")
	        --fi;

	        case io of -- este case es para probar el case no tiene nada que ver con el caso de prueba
	            tg :IO => out_string("es de tipo dinamico mas justo IO");
	            tg : Object => out_string("es de tipo dinamico mas justo Object");
	            tg : Complex => out_string("es de tipo dinamico mas justo Complex");
	        esac;
	        -- trivially equal (see CoolAid)
	        if c.reflect_X() = c.reflect_0() -- ver que en este = se hace por referencia osea si tienen la misma direccion en memoria
	        then out_string("=)\n")
	        else out_string("=(\n")
	        fi;
		-- equal
	        if c.reflect_X().reflect_Y().equal(c.reflect_0()) -- Aqui si se hace un equal por valor y resulta que reflejar por x y despues por Y es lo mismo que reflejar por 0, claro no?
	        then out_string("=)\n")
	        else out_string("=(\n")
	        fi;
	    }
	)
    };
};

class Complex inherits IO {
    x : Int;
    y : Int;

    init(a : Int, b : Int) : Complex {
	{
	    x = a;
	    y = b;
	    self;
	}
    };

    print() : Object {
	if y = 0
	then out_int(x)
	else out_int(x).out_string("+").out_int(y).out_string("I")
	fi
    };

    reflect_0() : Complex {
	{
	    x = ~x;
	    y = ~y;
	    self;
	}
    };

    reflect_X() : Complex {
	{
	    y = ~y;
	    self;
	}
    };

    reflect_Y() : Complex {
	{
	    x = ~x;
	    self;
	}
    };

    equal(d : Complex) : Bool {
	if x = d.x_value()
	then
	    if y = d.y_value()
	    then true
	    else false
	    fi
	else false
	fi
    };

    x_value() : Int {
	x
    };

    y_value() : Int {
	y
    };
};
