# Example application with Taipy 

### Taipy is an innovative Python framework designed to simplify the creation of interactive and visually engaging data fucused, BI and data science applications

---

### How to run it locally?

First setup new Python virtual environment at venv folder and install required components:

`source ./01_create_venv.sh`

Then you are ready to run an application:

`./02_run_app.sh`

Finally open an URL [http://localhost:3000](http://localhost:3000) at the browser.

---

### Run with Podman/Docker

Buld container image:

`podman build -t taipy-co2-emission -f Dockerfile .`

Run your newly built container image:

`podman run -d -p 3000:3000 --name taipy-co2-emission localhost/taipy-co2-emission`

Open an URL [http://localhost:3000](http://localhost:3000) at the browser.

---

Data delivered thanks to OWID: https://ourworldindata.org
