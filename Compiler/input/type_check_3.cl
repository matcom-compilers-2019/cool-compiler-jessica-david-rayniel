class Main inherits IO {
    c : Complex <- new Complex;
    main() : SELF_TYPE {
	{
	    c.init(1,1);
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

class New_Complex inherits Complex {
   z : Int;
   init (i : Int, j : Int, m : Int) : Complex{ -- SE esta redefiniendo pero la signatura para la cantidad de parametros no es correcta, da error
   {
    x <- i;
    y <- j;
    z <- m;
    self;
   }

   };

}

};