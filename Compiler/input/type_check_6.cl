class Main inherits IO {
    c : Complex <- new Complex;
    main() : SELF_TYPE {
	{
	    c.init(1,1,5); -- El metodo init recibe 2 parametros no 3.
	    c.reflect_0();
	    c.print();
	    out_string("Done");
	}
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
};
