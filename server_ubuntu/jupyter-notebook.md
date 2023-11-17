
[Ссылка на статью](https://towardsdatascience.com/run-jupyter-notebook-as-a-background-service-on-ubuntu-c5d6298ed1e)

Код запуска фоновым процессом
```
nohup jupyter-notebook --no-browser --port=8888 &
```
При создании пишится PID

Для закрытия процесса необходим PID код процесса.

Можно получить PIF с помощью `netstat -plnut`

или используя `ps`

```
$ ps au | grep jupyter
```

и что бы удалить процесс

```
$ kill -9 <PID>
```