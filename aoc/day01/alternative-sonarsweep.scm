#| Reads input file |#
(define (read-file name)
  (let ((port (open-input-file name)))
    (let file ((x (read port)))
      (if (eof-object? x)
          (begin
            (close-input-port port)
            '())
          (cons x (file (read port)))))))

(define lines-read (read-file "infile.ss"))

#|Counts number of times the next element of the sequence increases from the
   previous |#
(define (count-increased sequence)
  (reduce (lambda (x y) (if x (+ 1 y) y))
          0
          (transform-if-inc sequence)))

(define reduce
  (lambda (f init seq)
    (if (null? seq)
        init
        (f (car seq) (reduce f init (cdr seq))))))

(define (transform-if-inc sequence)
  (map (lambda (x y) (< x y)) sequence (append (cdr sequence) (list 0))))


#|Sum three and three elements, and gather elements in new list|#
(define (sum-windows sequence)
  (if (null? (cddr sequence))
      '()
      (cons (+ (car sequence) (cadr sequence) (caddr sequence))
            (sum-windows (cdr sequence)))))


#| Driver code |#
(count-increased lines-read)
(count-increased (sum-windows lines-read))
