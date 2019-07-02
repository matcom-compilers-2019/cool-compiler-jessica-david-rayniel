class Main inherits IO {
    x: Int <- 5;
    y: Int <- 10;
    main() : SELF_TYPE {
	{
	    out_string((new Object).type_name().substr(4,1));
	    out_string((new IO).type_name().substr(1,1));
	    out_string("\n");
        out_int(x+y);
	}
    };
};

