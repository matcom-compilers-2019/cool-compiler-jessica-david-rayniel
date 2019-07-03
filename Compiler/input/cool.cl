class Main inherits IO {
    x: Int <- 5;
    y: Int <- 10;
    main() : SELF_TYPE {
	{
	    out_string((new Object).type_name()).out_string("Otro otro");
	    out_string("\n");
        out_int(x+y + 100);
	}
    };
};

