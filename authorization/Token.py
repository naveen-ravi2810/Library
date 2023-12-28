from jose import jwt

a = jwt.encode(claims={"name": "naveen"}, key="Somesecret", algorithm="HS256")
t = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVGhpbGFrIn0.bobdTdeIdK9YfhA8ajJhJrfRq_mXkPtlUpjZZVeQTQI"
b = jwt.decode(token=t, key="advadvSomesecret")
