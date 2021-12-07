(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s))
)

(define (caddr s) 
    (car (cddr s))
)

(define (ordered? s) 
    (cond
        ((null? (cdr s)) true)
        ((> (car s) (car (cdr s))) false)
        (else (ordered? (cdr s)))
    )
)

(define (square x) (* x x))

(define (pow base exp) 
    (cond 
        ((= exp 0) 1)
        ((odd? exp) (* (pow base (- exp 1)) base))
        (else (square (pow base (/ exp 2))))
    )
)
