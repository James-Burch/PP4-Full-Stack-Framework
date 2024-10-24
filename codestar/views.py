from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


@login_required
def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-tee_time')
    return render(request, 'booking_list.html', {'bookings': bookings})
