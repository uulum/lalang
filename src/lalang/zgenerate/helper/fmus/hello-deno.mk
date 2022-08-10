--% index/fmus
.,d(/mk)
	hello.ts,f(e=__FILE__=hello.ts)
	$* deno run --allow-net hello.ts
--#

--% hello.ts
import { serve } from "https://deno.land/std@0.83.0/http/server.ts";
for await (const req of serve(":8080")) {
  req.respond({ body: "Hello deno" });
}
--#
