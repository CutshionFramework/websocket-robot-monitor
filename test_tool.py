
import libs_64.__common as __common


def main():
    rc = jkrc.RC("192.168.0.140")
    rc.login()
    ret = rc.get_robot_status()
    print(ret)
    rc.logout()

if __name__ == '__main__':
    __common.init_env()
    import jkrc

    main()

