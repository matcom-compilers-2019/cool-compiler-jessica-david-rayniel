
class List {
   -- Define operations on empty lists.

   isNil() : Bool { true };

   head()  : Int { { abort(); 0; } };

   tail()  : List { { abort(); self; } };

   cons(i : Int) : List {
      (new Cons).init(i, self)
   };
   one() : Int { 1 };
};

class Cons inherits List {

   car : Int;	-- The element in this list cell

   cdr : List;	-- The rest of the list

   isNil() : Bool { false };

   head()  : Int { car };

   tail()  : List { cdr };

   init(i : Int, rest : List) : List {
      {
	 car <- i;
	 cdr <- rest;
	 self;
      }
   };

   one() : Int { 2 };
};


class Main inherits IO {

   mylist : List;
   value : Int;
   cons : Cons;
   print_list(l : List) : Object {
      if l.isNil() then out_string("\n")
                   else {
			   out_int(l.head());
			   out_string(" ");
			   print_list(l.tail());
		        }
      fi
   };

   main() : Object {
      {
	 mylist <- (new List).cons(1).cons(2).cons(3).cons(4).cons(5);
	 --out_int(mylist.head());
	 --cons <- new Cons;
	 --out_int(mylist.one());
	 --out_int(cons.one());

	 --if cons.isNil() then out_string("es nil")
	 --else out_string("no es nil")
	 --fi;

	 --if true then out_string("2 es mayor que 10")
	 --else out_string("2 es menor que 10")
	 --fi;
	 --if (not false) then out_string("primera") else out_string("segunda")
	 --fi;
	 while (  not mylist.isNil()) loop
	    {
	       print_list(mylist);
	       mylist <- mylist.tail();
	    }
	 pool;
      --print_list(mylist);
      }
   };

};



