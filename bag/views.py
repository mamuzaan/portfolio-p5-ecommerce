from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quentity of the specified product to the shopping bag"""

    quentity = int(request.POST.get('quentity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quentity
    else:
        bag[item_id] = quentity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
