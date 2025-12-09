program GrammSchmidt_test

real :: B(3,3)

B(:,1) = [1,-1,1]
B(:,2) = [1,1,0]
B(:,3) = [0,1,1]

call GrammSchmidt(B)

do i = 1, 3
    print'(3F5.1)', B(:,i)
    print*, ''
end do

contains
subroutine GrammSchmidt(B)
real, intent(inout) :: B(:,:)

integer :: n, i, j
real :: dv(size(B,2))

do i = 1, size(B,1)
    dv = 0
    do j = 1, i-1
        dv  = dv + proy(B(:,i),B(:,j))
    end do

    B(:,i) = B(:,i) - dv
end do 

end subroutine

function proy(u,v) result(w)
    real, intent(in) :: u(:), v(:)
    real :: w(size(u))
    
    w = dot_product(u,v) / dot_product(v,v) * v
end function
end program