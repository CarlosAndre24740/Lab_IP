from flask import Flask, render_template, request, redirect, url_for, flash, abort
from jinja2 import DictLoader

app = Flask(__name__)
app.secret_key = "cambia-esta-clave-en-produccion"

# ---------------------------------------------------------------
# "Base de datos" en memoria (se reinicia al cerrar el programa).
# Para algo real, cambia esto por SQLite / SQLAlchemy.
# ---------------------------------------------------------------
casas = [
    {"id": 1, "titulo": "Casa moderna con jardín", "ciudad": "Zacatecas", "precio": 2850000,
     "recamaras": 3, "banos": 2, "m2": 160, "emoji": "🏡",
     "descripcion": "Casa de dos niveles, cocina integral, cochera para 2 autos y jardín amplio.",
     "vendedor": "María López", "contacto": "492-555-0101"},
    {"id": 2, "titulo": "Casa céntrica remodelada", "ciudad": "Fresnillo", "precio": 1650000,
     "recamaras": 2, "banos": 1, "m2": 110, "emoji": "🏠",
     "descripcion": "A unos pasos del centro, recién remodelada, ideal para pareja o familia pequeña.",
     "vendedor": "Carlos Ramírez", "contacto": "493-555-0142"},
    {"id": 3, "titulo": "Residencia de lujo con alberca", "ciudad": "Guadalajara", "precio": 9400000,
     "recamaras": 5, "banos": 4, "m2": 420, "emoji": "🏘️",
     "descripcion": "Fraccionamiento privado, alberca, terraza, cuarto de servicio y seguridad 24h.",
     "vendedor": "Inmobiliaria Altavista", "contacto": "333-555-0188"},
    {"id": 4, "titulo": "Casa económica cerca de escuelas", "ciudad": "Fresnillo", "precio": 890000,
     "recamaras": 2, "banos": 1, "m2": 75, "emoji": "🏚️",
     "descripcion": "Excelente opción para primera vivienda. Aceptamos crédito Infonavit.",
     "vendedor": "Ana Torres", "contacto": "493-555-0177"},
]
siguiente_id = 5


@app.template_filter("dinero")
def dinero(valor):
    return "${:,.0f} MXN".format(valor)


# ---------------------------------------------------------------
# Plantillas HTML (incluidas aquí para tener todo en un solo archivo)
# ---------------------------------------------------------------
BASE = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block titulo %}CasaFácil{% endblock %}</title>
  <style>
    :root { --azul:#1d4ed8; --oscuro:#0f172a; --gris:#64748b; --claro:#f1f5f9; --verde:#16a34a; }
    * { box-sizing: border-box; }
    body { margin:0; font-family: system-ui, Arial, sans-serif; background:var(--claro); color:var(--oscuro); }
    header { background:var(--oscuro); color:#fff; padding:14px 24px; display:flex;
             justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; }
    header a { color:#fff; text-decoration:none; margin-left:18px; }
    header .logo { font-size:1.4rem; font-weight:700; margin:0; }
    main { max-width:1100px; margin:24px auto; padding:0 16px; }
    .hero { background:linear-gradient(135deg,#1d4ed8,#0ea5e9); color:#fff; border-radius:14px;
            padding:32px 24px; margin-bottom:24px; }
    .hero h1 { margin:0 0 6px; }
    form.filtros { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:10px;
                   background:#fff; padding:16px; border-radius:12px; margin-bottom:24px; }
    input, select, textarea { width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:8px; font:inherit; }
    label { font-size:.85rem; color:var(--gris); display:block; margin-bottom:4px; }
    button, .btn { background:var(--azul); color:#fff; border:0; padding:11px 18px; border-radius:8px;
                   cursor:pointer; font:inherit; text-decoration:none; display:inline-block; }
    button:hover, .btn:hover { opacity:.9; }
    .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:18px; }
    .card { background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,.08); }
    .card .foto { background:#e0f2fe; font-size:4rem; text-align:center; padding:26px 0; }
    .card .info { padding:14px; }
    .precio { color:var(--verde); font-weight:700; font-size:1.2rem; }
    .datos { color:var(--gris); font-size:.9rem; margin:6px 0 12px; }
    .panel { background:#fff; padding:24px; border-radius:12px; margin-bottom:18px; }
    .flash { background:#dcfce7; border:1px solid #86efac; padding:12px; border-radius:8px; margin-bottom:16px; }
    .error { background:#fee2e2; border-color:#fca5a5; }
    .fila { display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:14px; margin-bottom:14px; }
    footer { text-align:center; color:var(--gris); padding:30px; }
  </style>
</head>
<body>
  <header>
    <p class="logo">🏡 CasaFácil</p>
    <nav>
      <a href="{{ url_for('inicio') }}">Comprar</a>
      <a href="{{ url_for('vender') }}">Vender mi casa</a>
    </nav>
  </header>
  <main>
    {% with mensajes = get_flashed_messages(with_categories=true) %}
      {% for categoria, texto in mensajes %}
        <div class="flash {{ 'error' if categoria == 'error' else '' }}">{{ texto }}</div>
      {% endfor %}
    {% endwith %}
    {% block contenido %}{% endblock %}
  </main>
  <footer>© 2026 CasaFácil · Compra y venta de casas</footer>
</body>
</html>
"""

INICIO = """
{% extends "base.html" %}
{% block contenido %}
<div class="hero">
  <h1>Encuentra la casa de tus sueños</h1>
  <p>Explora casas en venta o publica la tuya en minutos.</p>
</div>

<form class="filtros" method="get" action="{{ url_for('inicio') }}">
  <div><label>Ciudad</label>
    <input name="ciudad" placeholder="Ej. Fresnillo" value="{{ filtros.ciudad }}"></div>
  <div><label>Precio máximo (MXN)</label>
    <input name="precio_max" type="number" min="0" placeholder="3000000" value="{{ filtros.precio_max }}"></div>
  <div><label>Recámaras (mínimo)</label>
    <select name="recamaras">
      <option value="">Cualquiera</option>
      {% for n in [1,2,3,4,5] %}
        <option value="{{ n }}" {{ 'selected' if filtros.recamaras == n|string else '' }}>{{ n }}+</option>
      {% endfor %}
    </select></div>
  <div style="align-self:end"><button type="submit">Buscar</button></div>
</form>

<p>{{ lista|length }} casa(s) encontrada(s)</p>
<div class="grid">
  {% for c in lista %}
  <div class="card">
    <div class="foto">{{ c.emoji }}</div>
    <div class="info">
      <strong>{{ c.titulo }}</strong>
      <div class="precio">{{ c.precio|dinero }}</div>
      <div class="datos">📍 {{ c.ciudad }} · 🛏 {{ c.recamaras }} · 🚿 {{ c.banos }} · 📐 {{ c.m2 }} m²</div>
      <a class="btn" href="{{ url_for('detalle', casa_id=c.id) }}">Ver detalles</a>
    </div>
  </div>
  {% else %}
    <p>No hay casas con esos filtros.</p>
  {% endfor %}
</div>
{% endblock %}
"""

DETALLE = """
{% extends "base.html" %}
{% block titulo %}{{ c.titulo }} · CasaFácil{% endblock %}
{% block contenido %}
<div class="panel">
  <div style="font-size:5rem">{{ c.emoji }}</div>
  <h1>{{ c.titulo }}</h1>
  <div class="precio" style="font-size:1.6rem">{{ c.precio|dinero }}</div>
  <p class="datos">📍 {{ c.ciudad }} · 🛏 {{ c.recamaras }} recámaras · 🚿 {{ c.banos }} baños · 📐 {{ c.m2 }} m²</p>
  <p>{{ c.descripcion }}</p>
  <p><strong>Vendedor:</strong> {{ c.vendedor }} · <strong>Tel:</strong> {{ c.contacto }}</p>
</div>

<div class="panel">
  <h2>¿Te interesa? Contacta al vendedor</h2>
  <form method="post" action="{{ url_for('contactar', casa_id=c.id) }}">
    <div class="fila">
      <div><label>Tu nombre</label><input name="nombre" required></div>
      <div><label>Tu teléfono o correo</label><input name="contacto" required></div>
    </div>
    <label>Mensaje</label>
    <textarea name="mensaje" rows="3" required>Hola, me interesa esta casa. ¿Sigue disponible?</textarea>
    <br><br><button type="submit">Enviar mensaje</button>
  </form>
</div>
<a href="{{ url_for('inicio') }}">← Volver al catálogo</a>
{% endblock %}
"""

VENDER = """
{% extends "base.html" %}
{% block titulo %}Vender mi casa · CasaFácil{% endblock %}
{% block contenido %}
<div class="panel">
  <h1>Publica tu casa en venta</h1>
  <form method="post">
    <div class="fila">
      <div><label>Título del anuncio</label><input name="titulo" required value="{{ datos.get('titulo','') }}"></div>
      <div><label>Ciudad</label><input name="ciudad" required value="{{ datos.get('ciudad','') }}"></div>
      <div><label>Precio (MXN)</label><input name="precio" type="number" min="1" required value="{{ datos.get('precio','') }}"></div>
    </div>
    <div class="fila">
      <div><label>Recámaras</label><input name="recamaras" type="number" min="0" required value="{{ datos.get('recamaras','') }}"></div>
      <div><label>Baños</label><input name="banos" type="number" min="0" required value="{{ datos.get('banos','') }}"></div>
      <div><label>Metros cuadrados</label><input name="m2" type="number" min="1" required value="{{ datos.get('m2','') }}"></div>
    </div>
    <div class="fila">
      <div><label>Tu nombre</label><input name="vendedor" required value="{{ datos.get('vendedor','') }}"></div>
      <div><label>Teléfono de contacto</label><input name="contacto" required value="{{ datos.get('contacto','') }}"></div>
    </div>
    <label>Descripción</label>
    <textarea name="descripcion" rows="4" required>{{ datos.get('descripcion','') }}</textarea>
    <br><br><button type="submit">Publicar casa</button>
  </form>
</div>
{% endblock %}
"""

app.jinja_loader = DictLoader({
    "base.html": BASE,
    "inicio.html": INICIO,
    "detalle.html": DETALLE,
    "vender.html": VENDER,
})


# ---------------------------------------------------------------
# Rutas
# ---------------------------------------------------------------
@app.route("/")
def inicio():
    filtros = {
        "ciudad": request.args.get("ciudad", "").strip(),
        "precio_max": request.args.get("precio_max", "").strip(),
        "recamaras": request.args.get("recamaras", "").strip(),
    }
    lista = casas
    if filtros["ciudad"]:
        lista = [c for c in lista if filtros["ciudad"].lower() in c["ciudad"].lower()]
    if filtros["precio_max"].isdigit():
        lista = [c for c in lista if c["precio"] <= int(filtros["precio_max"])]
    if filtros["recamaras"].isdigit():
        lista = [c for c in lista if c["recamaras"] >= int(filtros["recamaras"])]
    return render_template("inicio.html", lista=lista, filtros=filtros)


@app.route("/casa/<int:casa_id>")
def detalle(casa_id):
    casa = next((c for c in casas if c["id"] == casa_id), None)
    if casa is None:
        abort(404)
    return render_template("detalle.html", c=casa)


@app.route("/casa/<int:casa_id>/contactar", methods=["POST"])
def contactar(casa_id):
    casa = next((c for c in casas if c["id"] == casa_id), None)
    if casa is None:
        abort(404)
    # Aquí podrías guardar el mensaje o enviar un correo al vendedor.
    flash(f"¡Mensaje enviado! {casa['vendedor']} se pondrá en contacto contigo.")
    return redirect(url_for("detalle", casa_id=casa_id))


@app.route("/vender", methods=["GET", "POST"])
def vender():
    global siguiente_id
    if request.method == "POST":
        datos = request.form.to_dict()
        try:
            nueva = {
                "id": siguiente_id,
                "titulo": datos["titulo"].strip(),
                "ciudad": datos["ciudad"].strip(),
                "precio": int(datos["precio"]),
                "recamaras": int(datos["recamaras"]),
                "banos": int(datos["banos"]),
                "m2": int(datos["m2"]),
                "emoji": "🏠",
                "descripcion": datos["descripcion"].strip(),
                "vendedor": datos["vendedor"].strip(),
                "contacto": datos["contacto"].strip(),
            }
        except (KeyError, ValueError):
            flash("Revisa los datos: hay campos vacíos o con números inválidos.", "error")
            return render_template("vender.html", datos=datos)
        casas.insert(0, nueva)
        siguiente_id += 1
        flash("¡Tu casa fue publicada con éxito!")
        return redirect(url_for("detalle", casa_id=nueva["id"]))
    return render_template("vender.html", datos={})


if __name__ == "__main__":
    app.run(debug=True)