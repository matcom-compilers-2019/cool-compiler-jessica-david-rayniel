class Main inherits IO {
    st : String;

    test(s : String) : Object{
    {
        out_string(s);
	    out_string("\n");
	    out_string(s.substr(0,1));
	    out_string("\n");
	    out_int(s.length());
	    out_int(s.length() -1);
	    out_string(s.substr(s.length() -1, 1));
	    out_string("\n");
	    out_string("\n");
    }
    };
    pal(s : String) : Bool {
	{

	    --test(s);
	    if s.length() = 0
	    then true
	    else if s.length() = 1
	    then true
	    else if s.substr(0, 1) = s.substr(s.length() - 1, 1)
	    then pal(s.substr(1, s.length() -2))
	    else false
	    fi fi fi;
    }
    };

    i : Int;
    io : IO;
    ob : Object;
    main() : SELF_TYPE {
	{
            i <- ~1;
        --io <- new IO;
        --ob <- new Object;
        --out_string(io.type_name());
        --out_string(ob.type_name());
        --out_string(i.type_name());
        --out_int("a".length());
        --i <- in_int();
        --out_int(i);

        --out_int(st.length());
        --out_string("\n");
        --out_string("\n");
        --out_string(st.substr(0,1));
        --out_string("\n");
        --out_string(st.substr(0,2));
        --out_string("\n");
        --out_string(st.substr(0,3));
        --out_string("\n");
        --out_string(st.substr(0,4));
        --out_string("\n");
        --out_string(st.substr(0,5));
        --out_string("\n");
        --out_string(st.substr(1,1));
        --out_string("\n");
        --out_string(st.substr(4,1));
        --out_string("\n");
        --out_string(st.substr(5,1));
        --out_string("\n");
        --out_string(st.substr(6,1));
        --out_string("\n");
        --out_int(st.length());
        --out_string(in_string());
	    out_string("enter a string\n");
	    st <- in_string();
	    --out_int("".length());
	    if pal(st)
	    then out_string("that was a palindrome\n")
	    else out_string("that was not a palindrome\n")
	    fi;
	}
    };
};
