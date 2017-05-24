from flask import redirect, render_template, request, url_for, Blueprint
from project.benefits.forms import NewBenefitForm
from project.models import Benefit
from project import db


benefits_blueprint = Blueprint(
	'benefits',
	__name__,
	template_folder='templates'
)

@benefits_blueprint.route("/", methods=['GET','POST'])
def index():
	if request.method =="POST":
		form = NewBenefitForm(request.form)
		if form.validate_on_submit():
			new_benefit = Benefit(form.name.data,form.cost_per_employee.data)
			db.session.add(new_benefit)
			db.session.commit()
			return redirect(url_for('benefits.index'))
		else:
			render_template('benefits/new.html', form=form)

	return render_template('benefits/index.html', benefits=Benefit.query.all())

@benefits_blueprint.route("/new")
def new():
	 return render_template('benefits/new.html', form=NewBenefitForm())


@benefits_blueprint.route('/<int:id>', methods=['GET','PATCH', 'DELETE'])
def show(id):
	found_benefit = Benefit.query.get(id)
	if request.method==b'DELETE':
		 db.session.delete(found_benefit)
		 db.session.commit()
		 return redirect(url_for('benefits.index'))
	if request.method ==b'PATCH':
		 form = NewBenefitForm(request.form)
		 if form.validate():
			 found_benefit.name = form.name.data
			 found_benefit.cost_per_employee = form.name.cost_per_employee
			 db.session.add(found_benefit)
			 db.session.commit()
			 return redirect(url_for('benefits.index', benefit=found_benefit))
		 else:
             #This the cause of the error.  Notice that the edit view needs a benefit passed
             #in.  Also make sure to setup a flash message.
			 return render_template('benefits/edit.html', benefit=found_benefit, form=form)
	return render_template('benefits/show.html', benefit=found_benefit)


@benefits_blueprint.route("/<int:id>/edit", methods=['GET'])
def edit(id):
	found_benefit =Benefit.query.get(id)
	form = NewBenefitForm()
	return render_template('benefits/edit.html', benefit = found_benefit, form = form)
