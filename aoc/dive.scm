#| Reads input file |#
(define (read-file name)
  (let ((port (open-input-file name)))
    (let file ((x (read port)))
      (if (eof-object? x)
          (begin
            (close-input-port port)
            '())
          (cons x (file (read port)))))))

(define lines-read (read-file "infile2.ss"))


(define make-sub
  (let ((depth 0)
        (horizontal-position 0)
        (aim 0))
    (lambda ()

      (define dispatch
        (lambda (message . value)
          
          (cond ((eq? message 'forward) (set! horizontal-position (+ horizontal-position (car value)))
                                        (set! depth (+ depth (* aim (car value))))
                                        horizontal-position)
                ((eq? message 'down) (set! aim (+ aim (car value)))
                                     aim)
                ((eq? message 'up) (set! aim (- aim (car value)))
                                   aim)

                ((eq? message 'solution-1) (* aim horizontal-position))
                ((eq? message 'solution-2) (* depth horizontal-position)))))

      dispatch)))

(define (steer-sub submarine lines-read)
  (if (null? lines-read)
      submarine
      (let ((command (car lines-read))
            (value (cadr lines-read)))
        (submarine command value)
        (steer-sub submarine (cddr lines-read)))))

(define (solve lines-read)
  (define submarine (make-sub))
  (steer-sub submarine lines-read)
  (cons (submarine 'solution-1) (submarine 'solution-2)))


(define solution (solve lines-read))

(display "Solution 1 : ")
(car solution)
(newline)

(display "Soltion 2 : ")
(cdr solution)
